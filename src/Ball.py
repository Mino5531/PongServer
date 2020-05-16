import const
import Racket
from random import uniform


class Ball:
    WIDTH, HEIGHT = 21, 19

    def __init__(self, game):
        self.myGame = game
        self.x = const.SCREENWIDTH//2
        self.y = const.SCREENHEIGHT//2
        self.xVel = 2
        self.yVel = 2
        self.speed = 0.5
        self.hitTimeout = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def Reset(self, yVel):
        self.setX(int(const.SCREENWIDTH/2))
        self.setY(int(const.SCREENHEIGHT/2))
        self.speed = 1
        self.yVel = yVel

    def act(self):
        if(self.hitTimeout > 0):
            self.hitTimeout -= 1
        x = self.getX()
        y = self.getY()
        leftRacket_x = self.myGame.LeftRacket.x
        leftRacket_y = self.myGame.LeftRacket.y
        rightRacket_x = self.myGame.RightRacket.x
        rightRacket_y = self.myGame.RightRacket.y
        self.setX(int(x+self.xVel*self.speed))
        self.setY(int(y+self.yVel*self.speed))
        # x += xVel * speed;
        # y += yVel *speed;
        if (x+self.WIDTH/2 + self.xVel * self.speed > const.SCREENWIDTH):
            self.speed = 0
            self.myGame.leftScore.addScore()
            self.Reset(1)
            # col right
        if (x + self.xVel * self.speed < 0):
            self.speed = 0
            self.myGame.rightScore.addScore()
            self.Reset(-1)
            # col left
        if (y+self.HEIGHT/2 + self.yVel * self.speed > const.SCREENHEIGHT or y-self.HEIGHT/2 + self.yVel * self.speed < 0):
            if(self.hitTimeout == 0):
                self.yVel *= -1
                self.hitTimeout = 5
            # self.speed += 0.1;

        # colliding with rightRacket?
        if(Ball.WIDTH//2+x+self.xVel * self.speed >= rightRacket_x - Racket.Racket.WIDTH//2 and x-Ball.WIDTH//2+self.xVel * self.speed <= rightRacket_x + Racket.Racket.WIDTH//2 and y+self.HEIGHT/2 + self.yVel * self.speed <= rightRacket_y + Racket.Racket.HEIGHT//2 and y-self.HEIGHT/2 + self.yVel * self.speed >= rightRacket_y - Racket.Racket.HEIGHT//2):
            if(self.hitTimeout == 0):
                self.xVel *= -1
                self.speed += uniform(0.1, 0.3)
                self.hitTimeout = 10

        # colliding with leftRacket?
        if(x+Ball.WIDTH//2+self.xVel * self.speed >= leftRacket_x - Racket.Racket.WIDTH//2 and x-Ball.WIDTH//2+self.xVel * self.speed <= leftRacket_x + Racket.Racket.WIDTH//2 and y+self.HEIGHT/2 + self.yVel * self.speed <= leftRacket_y + Racket.Racket.HEIGHT//2 and y-self.HEIGHT/2 + self.yVel * self.speed >= leftRacket_y - Racket.Racket.HEIGHT//2):
            if(self.hitTimeout == 0):
                self.xVel *= -1
                self.speed += uniform(0.1, 0.3)
                self.hitTimeout = 10
