from DataBuffer import DataBuffer
from DataHandler import DataHandler
import NetworkManager
import threading
import thread


class Client:
    def __init__(self, socket, address):
        self.sock = socket
        self.address = address
        self.name = ""
        self.inQueue = False
        self.listen = True
        self.game = None

        self.listenThread = threading.Thread(target=self.Listen, args=())
        self.listenThread.setDaemon(True)
        self.listenThread.start()

    def __del__(self):
        if(self.game != None):
            self.game.cancelGame()
        print("%s:%i disconnected" % (self.address[0], self.address[1]))

    def Listen(self):
        while(self.listen):
            data = self.sock.recv(1024)
            if (len(data) == 0):
                NetworkManager.NetworkManager.clients.pop(self.address)
                self.listen = False
                self.__del__()
                return
            buff = DataBuffer(data)
            if(buff.ReadInteger(False) in DataHandler.handlers):
                thread.start_new_thread(
                    DataHandler.handlers[buff.ReadInteger()], (data, self))
            else:
                print("Unknown packettype from %s:%i" %
                      (self.address[0], self.address[1]))

    def send(self, data):
        try:
            self.sock.send(data)
        except:
            print("Error while sending packet to %s:%i" %
                  (self.address[0], self.address[1]))
