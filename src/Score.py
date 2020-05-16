import DataSender


class Score:
    def __init__(self, game):
        self.score = 0
        self.myGame = game

    def addScore(self):
        self.score += 1
        if(self.myGame.leftScore == self):
            DataSender.DataSender.SendScoreUpdate(self.myGame.client1,self.score,self.myGame.rightScore.score)
            DataSender.DataSender.SendScoreUpdate(self.myGame.client2,self.score,self.myGame.rightScore.score)
        else:
            DataSender.DataSender.SendScoreUpdate(self.myGame.client1,self.myGame.leftScore.score,self.score)
            DataSender.DataSender.SendScoreUpdate(self.myGame.client2,self.myGame.leftScore.score,self.score)

    def Reset(self):
        self.score = 0
