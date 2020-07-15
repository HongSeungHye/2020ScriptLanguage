class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]

    def addCard(self,c):
        self.cards.append(c)

    def reset(self):
        self.cards.clear()






