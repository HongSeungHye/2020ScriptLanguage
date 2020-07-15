class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
        self.N=0 #카드의 갯수
    def inHand(self):
        #플레이어가 손에 들고있는 카드의 개수
        return self.N
    def addCard(self,c):
        self.cards.append(c)
        self.N+=1 #내가 갖고있는 카드의 개수 하나 증가
    def reset(self):
        self.N=0
        self.cards.clear()
    def value(self):
        # ace는 1 혹은 11로 모두 사용 가능
        # 일단 11로 계산한 후 21이 넘어가면 1로 정정 (즉,10을뺀다)
        #카드를 전부 더해서 숫자를 반환
        sum=0
        for i in range(self.N):
            if self.cards[i].getValue() == 1:
                sum += 11
                if sum > 21:
                    sum -= 10
            else:
                sum += self.cards[i].getValue()
        return sum





