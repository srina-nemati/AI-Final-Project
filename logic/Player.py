import enum


class BeeKind(enum.Enum):
    QueenBee = 0
    Beetle = 1
    Grasshopper = 2
    Spider = 3
    Ant = 4


class Player():
    def __init__(self, color):
        self.color = color
        self.is_queen_placed = False
        self.pieces = {
            BeeKind.QueenBee: 1,
            BeeKind.Spider: 2,
            BeeKind.Ant: 3,
            BeeKind.Grasshopper: 3,
            BeeKind.Beetle: 2
        }

    def get_player_pieces(self):
        return self.pieces

    def return_one_piece(self, str_inp):
        if str_inp == 'Q':
            self.pieces[BeeKind.QueenBee] += 1
        if str_inp == 'B':
            self.pieces[BeeKind.Beetle] += 1
        if str_inp == 'G':
            self.pieces[BeeKind.Grasshopper] += 1
        if str_inp == 'A':
            self.pieces[BeeKind.Ant] += 1
        if str_inp == 'S':
            self.pieces[BeeKind.Spider] += 1

    def use_one_piece(self, str_inp):
        if str_inp == 'Q':
            if self.pieces[BeeKind.QueenBee] > 0:
                self.is_queen_placed = True
                self.pieces[BeeKind.QueenBee] -= 1
        elif str_inp == 'B':
            if self.pieces[BeeKind.Beetle] > 0:
                self.pieces[BeeKind.Beetle] -= 1
        elif str_inp == 'G':
            if self.pieces[BeeKind.Grasshopper] > 0:
                self.pieces[BeeKind.Grasshopper] -= 1
        elif str_inp == 'A':
            if self.pieces[BeeKind.Ant] > 0:
                self.pieces[BeeKind.Ant] -= 1
        elif str_inp == 'S':
            if self.pieces[BeeKind.Spider] > 0:
                self.pieces[BeeKind.Spider] -= 1

    def has_enough_piece(self, str_inp):
        if str_inp == 'Q':
            return self.pieces[BeeKind.QueenBee] > 0
        elif str_inp == 'B':
            return self.pieces[BeeKind.Beetle] > 0
        elif str_inp == 'G':
            return self.pieces[BeeKind.Grasshopper] > 0
        elif str_inp == 'A':
            return self.pieces[BeeKind.Ant] > 0
        elif str_inp == 'S':
            return self.pieces[BeeKind.Spider] > 0
        return False

# if __name__ == '__main__':
#     p = Player("w")
#     p.use_one_piece('Q')
#     print(p.pieces[BeeKind.QueenBee])
