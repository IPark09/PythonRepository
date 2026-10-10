import time

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
        self.board_type = board_type
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

    def has_moves(self, color):
        step = -1 if color == "white" else 1
        for chkr in self.checkers:
            if chkr.get_color() != color:
                continue
            r, c = chkr.get_cords()
            for d in (1, 2):
                for dc in (-d, d):
                    if self.check_move(r, c, r + step*d, c + dc, color, color) != 0:
                        return True
        return False

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
        print(f"Game {self.status}!\nTotal checkers still present: {len(self.checkers)}\nTotal checkers eliminated: {len(self.removed)}")

    def show(self):
        w = len(str(self.size_col - 1)) + 1
        print("State of the board:")
        out = " " * w
        for k in range(self.size_col): out += f"{k:>{w}}"
        for i in range(self.size_row):
            out += f"\n{i:>{w}}"
            for j in range(self.size_col):
                ch = self.find_checker(i, j)
                if ch is not None:
                    if ch.get_color() == "white": sym = "W"
                    else: sym = "B"
                else: sym = "–"
                out += f"{sym:>{w}}"
        print(out)
                

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.move_num = 0
        self.result = "playing"
        self.timer = 0
        self.points = 0

    def define_result(self, pts, tmr):
        if self.points > pts:
            self.result = "won"
        elif self.points < pts:
            self.result = "lost"
        elif tmr > self.timer:
            self.result = "won"
        elif tmr < self.timer:
            self.result = "lost"
        else: self.result = "draw"
        return self.result

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

    def print_data(self):
        print(f"Your color: {self.color}\nYour points: {self.points}\nTime spent: {self.timer:.1f}s\nMoves made: {self.move_num}")

    def get_pNt(self):
        return self.points, self.timer


class Game:
    def __init__(self):
        self.total_time = 0
        self.total_moves = 0
        self.curr_color = "white"
        self.players = []
        self.board = None

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
        return res

    def move_loop(self, stamp):
        mv = None
        while (True):
            mv = input("Enter the position of a checker and where you want to move it (template – 'row1 column1 row2 column2'): ").split()
            if len(mv) == 4 and mv[0].isdecimal() and mv[1].isdecimal() and mv[2].isdecimal() and mv[3].isdecimal():
                r1, c1, r2, c2 = map(int, mv)
                res = self.move(r1, c1, r2, c2, time.time()-stamp)
                if res == 2:
                    print("Success. +1 point!")
                    break
                elif res == 1:
                    print("Success.")
                    break
                print("Wrong move. Try again.")
            else: print("Try again.")

    def finalizing(self):
        self.board.finish()
        print(f"Total game time: {self.total_time:.1f}s\nTotal moves performed: {self.total_moves}")
        nm1 = self.players[0].get_name()
        print(f"Information for {nm1}:")
        self.players[0].print_data()
        nm2 = self.players[1].get_name()
        print(f"Information for {nm2}:")
        self.players[1].print_data()
        print("VERDICT:")
        p1,t1 = self.players[0].get_pNt()
        p2,t2 = self.players[1].get_pNt()
        print(f"{nm1} {self.players[0].define_result(p2,t2)}!")
        print(f"{nm2} {self.players[1].define_result(p1,t1)}!")                

    def game_loop(self):
        while(True):
            stamp = time.time()
            plr = self.find_player()
            if not self.board.has_moves(self.curr_color):
                print(f"{plr.get_name()} has no moves left. Ending the session.")
                self.finalizing()
                break
            print(f"{plr.get_name()}'s turn.")
            plr.print_data()
            inp = input("Do you want to stop the game? If yes – enter 's': ").lower()
            if inp == "s":
                self.finalizing()
                break
            else:
                self.board.show()
            self.move_loop(stamp)

    def gaming(self):
        print("\n\nWelcome to the Checkers! Please choose a size of a board.")
        inp = None
        while (True):
            inp = input("Input 's' for a 8x8 small board or 'b' for a 12x12 big board: ").lower()
            if (inp == "s") or (inp == "b"): break
            else: print("Please try again.")
        if inp == "s": self.board = Board("small")
        else: self.board = Board("big")
        plr1 = None
        plr2 = None
        while (True):
            plr1 = input("Input a name and a color ('b' – black, 'w' – white) for a player #1 (template – 'name color'): ").split()
            if len(plr1)==2 and plr1[1].lower() in ("w","b"): break
            else: print("Please try again.")
        while (True):
            plr2 = input("Input a name for a player #2: ")
            if plr2: break
            else: print("Please try again.")
        if plr1[1].lower() == "w":
            self.players.append(Player(plr1[0], "white"))
            self.players.append(Player(plr2, "black"))
        else:
            self.players.append(Player(plr1[0], "black"))
            self.players.append(Player(plr2, "white"))
        print(f"The game begins!\n\n")
        self.game_loop()