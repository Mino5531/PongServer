from DataBuffer import DataBuffer


class ServerPackets:
    s_EnterGame = 1
    s_SendGamePositions = 2
    s_SendScore = 3
    s_StopGame = 4


class DataSender:
    @staticmethod
    def SendGame(client, game):
        buff = DataBuffer()
        buff.WriteObject(ServerPackets.s_EnterGame)
        if(client == game.client1):
            buff.WriteObject(game.client2.name)
            buff.WriteObject(True)
        else:
            buff.WriteObject(game.client1.name)
            buff.WriteObject(False)
        # buff.WriteObject(game.gameID)
        buff.WriteObject(int(game.LeftRacket.x))
        buff.WriteObject(int(game.LeftRacket.y))
        buff.WriteObject(int(game.RightRacket.x))
        buff.WriteObject(int(game.RightRacket.y))
        client.send(buff.ToArray())

    @staticmethod
    def SendPositionData(client, left_x, left_y, right_x, right_y, ball_x, ball_y):
        buff = DataBuffer()
        buff.WriteObject(ServerPackets.s_SendGamePositions)
        buff.WriteObject(int(left_x))
        buff.WriteObject(int(left_y))
        buff.WriteObject(int(right_x))
        buff.WriteObject(int(right_y))
        buff.WriteObject(int(ball_x))
        buff.WriteObject(int(ball_y))
        client.send(buff.ToArray())

    @staticmethod
    def SendScoreUpdate(client, leftScore, rightScore):
        buff = DataBuffer()
        buff.WriteObject(ServerPackets.s_SendScore)
        buff.WriteObject(leftScore)
        buff.WriteObject(rightScore)
        client.send(buff.ToArray())

    @staticmethod
    def SendStopGame(client, msg):
        buff = DataBuffer()
        buff.WriteObject(ServerPackets.s_StopGame)
        buff.WriteObject(msg)
        client.send(buff.ToArray())
