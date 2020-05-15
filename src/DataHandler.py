from DataBuffer import DataBuffer
from QueueManager import QueueManager


class ClientPackets:
    c_SetName = 1
    c_EnterPlayerQueue = 2
    c_EnterAIQueue = 3
    c_LeavePlayerQueue = 4
    c_RacketPositionUpdate = 5


class DataHandler:
    handlers = {}

    @staticmethod
    def InitDataHandler():
        DataHandler.handlers[ClientPackets.c_SetName
                             ] = DataHandler.HandleNameSet

        DataHandler.handlers[ClientPackets.c_EnterPlayerQueue] = DataHandler.QueueEnterRequest
        DataHandler.handlers[ClientPackets.c_RacketPositionUpdate] = DataHandler.HandleRacketPosUpdate
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

    @staticmethod
    def HandleRacketPosUpdate(data, client):
        buff = DataBuffer(data)
        buff.SkipBytes(4)
        up = buff.ReadBoolean()
        if(client.game.client1 == client):
            if(up):
                client.game.LeftRacket.MoveUp()
            else:
                client.game.LeftRacket.MoveDown()
        else:
            if(up):
                client.game.RightRacket.MoveUp()
            else:
                client.game.RightRacket.MoveDown()
