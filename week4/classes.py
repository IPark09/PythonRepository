class Player:
    def __init__(self, name=None, color=None, move_num=None, result=None, time=None):
        self.name = name
        self.color = color
        self.move_num = move_num
        self.result = result
        self.time = time


class Checker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.alive = True
    
    def make_king(self):
        self.king = True

    def remove(self):
        self.alive = False

    def get_cords(self):
        return self.row, self.col

    def move(self, r2, c2):
        self.row = r2
        self.col = c2


class Board:
    def __init__(self, type):
        self.type = type.lower()
        self.status = "Ongoing"
        checkers = []
        self.size_row = 0
        self.size_col = 0
        self.board_refill(self)

    def board_refill(self):
        if self.type == "small":
            self.size_col = self.size_row = 8
        elif self.type == "big":
            self.size_col = self.size_row = 12
        for i in range(self.size_row):
            for j in range(self.size_col):
                if (i%2==0 and j%2!=0) or (i%2!=0 and j%2==0):
                    if i < self.size_row/2-1:
                        self.checkers.append(Checker(i, j, "black"))
                    elif i > self.size_row/2:
                        self.checkers.append(Checker(i, j, "white"))

    def finish(self):
        self.status = "Finished"

    def find_checker(self, r1, c1):
        for chkr in self.checkers:
            r, c = chkr.get_cords()
            if r==r1 and c==c1:
                return chkr
        return None

    def check_move(self, r1, c1, r2, c2):
        return True###checking logic

    def remove(self, r1, c1, r2, c2):
        chkr = self.find_checker(r1+(r2-r1)/2, c1+(c2-c1)/2)
        chkr.remove()###removal logic

    def move(self, r1, c1, r2, c2):
        chkr = self.find_checker(r1, c1)
        if chkr == None: return "Checker not found"
        if self.check_move(r1, c1, r2, c2):
            self.remove(r1, c1, r2, c2)
            chkr.move(r2, c2)
            return "Success"
        else:
            return "Wrong move"