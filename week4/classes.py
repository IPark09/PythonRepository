class Checker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
    
    def make_king(self):
        self.king = True

    def get_cords(self):
        return self.row, self.col

    def move(self, r2, c2):
        self.row = r2
        self.col = c2

    def get_color(self):
        return self.color

    def get_lvl(self):
        return self.king


class Board:
    def __init__(self, board_type):
        self.board_type = board_type.lower()
        self.status = None
        self.checkers = None
        self.removed = None
        self.size_row = None
        self.size_col = None
        self.board_refill()

    def board_refill(self):
        if self.board_type == "small":
            self.size_col = self.size_row = 8
        elif self.board_type == "big":
            self.size_col = self.size_row = 12
        else: raise ValueError("Unknown board type")
        self.checkers = []
        self.removed = []
        self.status = "ongoing"
        for i in range(self.size_row):
            for j in range(self.size_col):
                if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                    if i < self.size_row//2-1:
                        self.checkers.append(Checker(i, j, "black"))
                    elif i > self.size_row//2:
                        self.checkers.append(Checker(i, j, "white"))

    def find_checker(self, r1, c1):
        for chkr in self.checkers:
            r, c = chkr.get_cords()
            if r==r1 and c==c1:
                return chkr
        return None

    def check_move(self, r1, c1, r2, c2, chkr_color, user_color):
        if (chkr_color == user_color) and (0 <= c2 < self.size_col) and (0 <= r2 < self.size_row):
            step_col = c2-c1
            step_row = r2-r1
            if ((chkr_color == "white" and step_row < 0) or (chkr_color == "black" and step_row > 0)) and (self.find_checker(r2, c2) is None):
                if abs(step_col) == abs(step_row) == 1:
                    return 1
                elif abs(step_col) == abs(step_row) == 2:
                    chkr = self.find_checker(r1+(step_row)//2, c1+(step_col)//2)
                    if (chkr is not None) and (chkr.get_color()!=chkr_color):
                        return 2  
        return 0

    def remove(self, r1, c1, r2, c2):
        chkr = self.find_checker(r1+(r2-r1)//2, c1+(c2-c1)//2)
        self.removed.append(chkr)
        self.checkers.remove(chkr)

    def move(self, r1, c1, r2, c2, user_color):
        chkr = self.find_checker(r1, c1)
        if chkr is None: return 0
        flag = self.check_move(r1, c1, r2, c2, chkr.get_color(), user_color)
        if flag != 0:
            chkr.move(r2, c2)
            if flag == 2:
                self.remove(r1, c1, r2, c2)
            row, col = chkr.get_cords()
            if (not chkr.get_lvl()) and ((row == 0) or (row == self.size_row-1)):
                chkr.make_king()
        return flag

    def finish(self):
        self.status = "finished"

    def show(self):
        return 0 


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.move_num = 0
        self.result = "playing"
        self.timer = 0
        self.points = 0

    def set_result(self, result):
        self.result = result

    def increase_time(self, spent):
        self.timer += spent

    def get_color(self):
        return self.color

    def increase_moves(self):
        self.move_num += 1

    def increase_points(self):
        self.points += 1

    def get_name(self):
        return self.name


class Game:
    def __init__(self):
        self.total_time = 0
        self.total_moves = 0
        self.curr_color = "white"
        self.players = []
        self.board = None

    def add_player(self, name, color):
        self.players.append(Player(name, color))

    def create_board(self, board_type):
        self.board = Board(board_type)

    def find_player(self):
        player = None
        for p in self.players:
            if p.get_color() == self.curr_color:
                player = p
                break
        return player

    def move(self, r1, c1, r2, c2, spent):
        player = self.find_player()
        if player is None: raise ValueError("Player not found")
        res = self.board.move(r1, c1, r2, c2, self.curr_color)
        if res > 0:
            player.increase_moves()
            player.increase_time(spent)
            self.total_moves += 1
            self.total_time += spent
            if self.curr_color == "white": self.curr_color = "black"
            else: self.curr_color = "white"
            if res == 2:
                player.increase_points()
                return "Success. +1 point!"
            return "Success"
        return "Wrong move. Try again"

    def gaming(self):
        while(True):
            inp = input(f"{self.find_player().get_name()}'s turn: ")