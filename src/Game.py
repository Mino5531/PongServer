from DataSender import DataSender
from Racket import Racket
from Score import Score
from Ball import Ball
import threading
import sched
import time


class Game:
    __maxGameID = 0
    __maxGameIDMutex = threading.Lock()
    Games = []
    MaxY = 400
    MaxX = 600

    def __init__(self, client1, client2):
        self.client1 = client1
        self.client2 = client2
        self.client1.game = self
        self.client2.game = self
        Game.__maxGameIDMutex.acquire()
        self.gameID = Game.__maxGameID
        Game.__maxGameID += 1
        Game.__maxGameIDMutex.release()
        Game.Games.append(self)
        self.leftScore = Score(self)
        self.rightScore = Score(self)
        self.LeftRacket = Racket(False)  # racket of client 1
        self.RightRacket = Racket(True)  # racket of client 2
        self.ball = Ball(self)
        self.stop = False
        self.loopSched = sched.scheduler(time.time, time.sleep)
        DataSender.SendGame(self.client1, self)
        DataSender.SendGame(self.client2, self)
        print("Starting game for %s and %s" %
              (self.client1.name, self.client2.name))
        self.loopSched.enter(0.016, 1, self.gameLoop,
                             (self.loopSched,))  # gameLoop at 60Hz
        self.loopSched.run()

    def gameLoop(self, sched):  # gameLoop at 60Hz
        self.ball.act()
        DataSender.SendPositionData(self.client1, self.LeftRacket.x,
                                    self.LeftRacket.y, self.RightRacket.x, self.RightRacket.y, self.ball.getX(), self.ball.getY())
        DataSender.SendPositionData(self.client2, self.LeftRacket.x,
                                    self.LeftRacket.y, self.RightRacket.x, self.RightRacket.y, self.ball.getX(), self.ball.getY())
        if(self.rightScore.score > 9):
            DataSender.SendStopGame(self.client1, "You win!")
            DataSender.SendStopGame(self.client2, self.client1.name+" won!")
            self.__del__()
            return
        if(self.leftScore.score > 9):
            DataSender.SendStopGame(self.client2, "You win!")
            DataSender.SendStopGame(self.client1, self.client2.name+" won!")
            self.__del__()
            return
        if(self.stop):
            return
        sched.enter(0.016, 1, self.gameLoop, (sched,))  # gameLoop at 60Hz

    def cancelGame(self):
        self.stop = True
        try:
            DataSender.SendStopGame(self.client1, "Game aborted")
        except:
            pass
        try:
            DataSender.SendStopGame(self.client2, "Game aborted")
        except:
            pass
        self.__del__()

    def __del__(self):
        print("GameID: %i finished, cleaning up..." % (self.gameID))
        try:
            self.client1.game = None
        except:
            pass
        try:
            self.client2.game = None
        except:
            pass
        for i in range(len(Game.Games)):
            if(Game.Games[i] == self):
                Game.Games.pop(i)
