import const


class Racket:
    WIDTH, HEIGHT = 11, 164
    MAX_Y = const.SCREENHEIGHT-HEIGHT/2
    MIN_Y = HEIGHT/2
    SPEED = 5

    def __init__(self, isRight):
        self.y = Racket.MIN_Y
        if(isRight):
            self.x = 590
        else:
            self.x = 10

    def MoveUp(self):
        if(self.y - Racket.SPEED < Racket.HEIGHT/2):
            return
        self.y -= Racket.SPEED

    def MoveDown(self):
        if(self.y + Racket.SPEED > const.SCREENHEIGHT - Racket.HEIGHT/2):
            return
        self.y += Racket.SPEED

    def Reset(self):
        self.y = Racket.MIN_Y
