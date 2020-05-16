from time import sleep
from Game import Game
import threading
import thread


class QueueManager:
    instance = None
    __queueMutex = threading.Lock()

    def __init__(self):
        QueueManager.instance = self
        self.queueRunning = True
        self.queueThread = threading.Thread(target=self.ManageQueue, args=())
        self.__queue = []
        self.queueThread.setDaemon(True)
        self.queueThread.start()
        print("QueueManager initialized")
# --------------------------------------------------------

  ####            #  #   #
  #               # #    #
  ##   #  #  ###  ##     #
  #    #  #  #    # #
  #     ##   ###  #  #   #

# --------------------------------------------------------
    def AddToQueue(self, client):
        QueueManager.__queueMutex.acquire()
        try:
            self.__queue.append(client)
        finally:
            QueueManager.__queueMutex.release()
        print("%s is now in the pvp queue" % (client.name))

    def RemoveFromQueue(self, client):
        QueueManager.__queueMutex.acquire()
        try:
            for i in range(len(self.__queue)):
                if(self.__queue[i] == client):
                    self.__queue.pop(i)
                    break
        finally:
            QueueManager.__queueMutex.release()

    def ManageQueue(self):
        while(self.queueRunning):
            sleep(2)
            QueueManager.__queueMutex.acquire()
            try:
                if(len(self.__queue) >= 2):
                    while(len(self.__queue) >= 2):
                        thread.start_new_thread(
                            Game, (self.__queue[0], self.__queue[1]))
                        self.__queue.pop(0)
                        self.__queue.pop(0)
            finally:
                QueueManager.__queueMutex.release()
