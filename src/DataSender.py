from DataBuffer import DataBuffer


class ServerPackets:
    s_EnterGame = 1


class DataSender:
    @staticmethod
    def SendGame(client, game):
        buff = DataBuffer()
        buff.WriteObject(ServerPackets.s_EnterGame)
        if(client == game.client1):
            buff.WriteObject(game.client2.name)
        else:
            buff.WriteObject(game.client1.name)
        buff.WriteObject(game.gameID)
        
