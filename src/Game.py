from DataSender import DataSender
import threading


class Game:
    __maxGameID = 0
    __maxGameIDMutex = threading.Lock()
    Games = []
    MaxY = 400
    MaxX = 600

    def __init__(self, client1, client2):
        self.client1 = client1
        self.client2 = client2
        Game.__maxGameIDMutex.acquire()
        self.gameID = Game.__maxGameID
        Game.__maxGameID += 1
        Game.__maxGameIDMutex.release()
        Game.Games.append(self)
        DataSender.SendGame(self.client1, self)
        DataSender.SendGame(self.client2, self)

    def __del__(self):
        for i in range(len(Game.Games)):
            if(Game.Games[i] == self):
                Game.Games.pop(i)
