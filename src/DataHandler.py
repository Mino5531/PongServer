from DataBuffer import DataBuffer
from QueueManager import QueueManager


class ClientPackets:
    c_SetName = 1
    c_EnterPlayerQueue = 2
    c_EnterAIQueue = 3
    c_LeavePlayerQueue = 4


class DataHandler:
    handlers = {}

    @staticmethod
    def InitDataHandler():
        DataHandler.handlers[ClientPackets.c_SetName
                             ] = DataHandler.HandleNameSet

        DataHandler.handlers[ClientPackets.c_EnterPlayerQueue] = DataHandler.QueueEnterRequest
        print("DataHandler initialized")

    @staticmethod
    def HandleNameSet(data, client):
        buff = DataBuffer(data)
        buff.SkipBytes(4)
        client.name = buff.ReadString()
        print("%s:%i is now %s" %
              (client.address[0], client.address[1], client.name))

    @staticmethod
    def QueueEnterRequest(data, client):
        QueueManager.instance.AddToQueue(client)
