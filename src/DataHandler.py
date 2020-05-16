from DataBuffer import DataBuffer
from QueueManager import QueueManager


class ClientPackets:
    c_SetName = 1
    c_EnterPlayerQueue = 2
    c_EnterAIQueue = 3
    c_LeavePlayerQueue = 4
    c_RacketPositionUpdate = 5


class DataHandler:

    instance = None

    def __init__(self):
        DataHandler.instance = self
        self.handlers = {}
        self.handlers[ClientPackets.c_SetName
                      ] = self.HandleNameSet

        self.handlers[ClientPackets.c_EnterPlayerQueue] = self.QueueEnterRequest
        self.handlers[ClientPackets.c_RacketPositionUpdate] = self.HandleRacketPosUpdate
        print("DataHandler initialized")

    def HandleNameSet(self, data, client):
        buff = DataBuffer(data)
        buff.SkipBytes(4)
        client.name = buff.ReadString()
        print("%s:%i is now %s" %
              (client.address[0], client.address[1], client.name))

    def QueueEnterRequest(self, data, client):
        QueueManager.instance.AddToQueue(client)

    def HandleRacketPosUpdate(self, data, client):
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
