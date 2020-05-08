from DataBuffer import DataBuffer


class ClientPackets:
    c_SetName = 1
    c_EnterPlayerQueue = 2
    c_EnterAIQueue = 3


class DataHandler:
    handlers = {}

    @staticmethod
    def InitDataHandler():
        DataHandler.handlers[ClientPackets.c_SetName
                             ] = DataHandler.HandleNameSet

    @staticmethod
    def HandleNameSet(data, client):
        buff = DataBuffer(data)
        buff.SkipBytes(4)
        client.name = buff.ReadString()
