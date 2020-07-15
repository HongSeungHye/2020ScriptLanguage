from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
import random

class TexasHoldemPoker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Black Jack")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()  # 버튼 5개에 대해서 각각버튼마다 커맨드 연결한 함수
        self.setupLabel()  # 5개의 라벨들

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.community=Player("community")
        self.betMoney = 10
        self.playerMoney = 1000
        self.LcardsPlayer = []  # 이미지를 라벨로 표시한 리스트
        self.LcardsDealer = []  #딜러 카드 이미지 배열
        self.LcardsCommunity=[]
        self.deckN = 0  # 52장의 카드 랜덤하게 카드덱에서 뽑아낸다.
        self.nState= 0 # 커뮤니티 카드 몇장 나와있는지

        self.window.mainloop()

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)

        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2,
                            command=self.pressedAgain)
        self.Again.place(x=700, y=500)


        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $1000", width=15, height=1, font=self.fontstyle, bg="green", fg="orange")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerPts = Label(text="", width=15, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LplayerPts.place(x=300, y=400)
        self.LdealerPts = Label(text="", width=15, height=1, font=self.fontstyle2, bg="green", fg="white")
        self.LdealerPts.place(x=300, y=100)
        self.Lstatus = Label(text="", width=20, height=1, font=self.fontstyle2, bg="green", fg="red")
        self.Lstatus.place(x=600, y=300)

    def pressedCheck(self):
        self.checkState()

    def checkState(self):
        if self.nState==6:
            self.checkWinner()
            self.nState=0
            self.Check["state"] = "disabled"
            self.Check['bg'] = 'gray'
            self.Bx1["state"] = "disabled"
            self.Bx1['bg'] = 'gray'
            self.Bx2["state"] = "disabled"
            self.Bx2['bg'] = 'gray'
            self.Deal["state"] = "disabled"
            self.Deal['bg'] = 'gray'
            self.Again["state"] = "active"
            self.Again['bg'] = 'white'

        else :
            self.Check["state"] = "disabled"
            self.Check['bg'] = 'gray'
            self.Bx1["state"] = "disabled"
            self.Bx1['bg'] = 'gray'
            self.Bx2["state"] = "disabled"
            self.Bx2['bg'] = 'gray'
            self.Deal["state"] = "active"
            self.Deal['bg'] = 'white'
            self.Again["state"] = "disabled"
            self.Again['bg'] = 'gray'

    def pressedBx1(self):
        self.betMoney*=2
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= (self.betMoney // 2)
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney //= 2

        self.checkState()

    def pressedBx2(self):
        self.betMoney *= 3
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= (self.betMoney //3 *2)
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney //= 3

        self.checkState()

    def firstDeal(self):
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0  # 다음게임을 위해서 초기화

        # 첫 딜
        # 플레이어의 카드
        self.NewCards()
        self.player.addCard(self.newCard)
        self.LcardsPlayer.append(Label(self.window, image=self.p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[0].image = self.p
        # 플레이어가 가지고 있는 카드의 개수 -1 (카드인덱스는 0부터 시작하기때문)
        self.LcardsPlayer[0].place(x=50, y=350)

        self.NewCards()
        self.player.addCard(self.newCard)
        self.LcardsPlayer.append(Label(self.window, image=self.p))
        self.LcardsPlayer[1].image = self.p
        self.LcardsPlayer[1].place(x=50 + 80, y=350)

        # 딜러의 뒤집힌 카드
        self.NewCards()
        self.dealer.addCard(self.newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[0].image = p
        self.LcardsDealer[0].place(x=50, y=50)

        self.NewCards()
        self.dealer.addCard(self.newCard)
        p = PhotoImage(file="cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))
        self.LcardsDealer[1].image = p
        self.LcardsDealer[1].place(x=50 + 80, y=50)

    def Pluscommunity(self,n):
        self.NewCards()
        self.community.addCard(self.newCard)
        self.player.addCard(self.newCard)
        self.dealer.addCard(self.newCard)
        self.LcardsCommunity.append(Label(self.window,image=self.p))
        self.LcardsCommunity[n].image=self.p
        self.LcardsCommunity[n].place(x=250+n*80,y=200)

    def pressedDeal(self):
        if self.nState==0:
            self.firstDeal()
            self.nState+=1

        elif self.nState==1:
            for i in range(3):
                self.Pluscommunity(i)
                self.nState+=1
        else:
            self.Pluscommunity(self.nState-1)
            self.nState+=1


        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)

        self.Check["state"] = "active"
        self.Check['bg'] = 'white'
        self.Bx1["state"] = "active"
        self.Bx1['bg'] = 'white'
        self.Bx2["state"] = "active"
        self.Bx2['bg'] = 'white'
        self.Deal["state"] = "disabled"
        self.Deal['bg'] = 'gray'
        self.Again["state"] = "disabled"
        self.Again['bg'] = 'gray'
        print("커뮤니티카드리스트:",self.LcardsCommunity)
        print("플레이어카드리스트:", self.LcardsPlayer)
        print("딜러카드리스트:",self.LcardsDealer)



    def NewCards(self):
        self.newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.p = PhotoImage(file="cards/" + self.newCard.filename())

    def pressedAgain(self):
        self.nState=0
        self.Check["state"] = "active"
        self.Check['bg'] = 'white'
        self.Bx1["state"] = "active"
        self.Bx1['bg'] = 'white'
        self.Bx2["state"] = "active"
        self.Bx2['bg'] = 'white'
        self.Deal["state"] = "disabled"
        self.Deal['bg'] = 'gray'
        self.Again["state"] = "disabled"
        self.Again['bg'] = 'gray'

        for i in range(2):
            self.LcardsPlayer[i].destroy()
            self.LcardsDealer[i].destroy()
        for i in range(5):
            self.LcardsCommunity[i].destroy()

        self.LdealerPts.configure(text='')
        self.LplayerPts.configure(text='')
        self.Lstatus.configure(text='')

        self.betMoney = 10
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LcardsPlayer = []  # 이미지를 라벨로 표시한 리스트
        self.LcardsDealer = []
        self.LcardsCommunity=[]
        self.deckN = 0  # 52장의 카드 랜덤하게 카드덱에서 뽑아낸다
        self.player.reset()
        self.dealer.reset()
        self.community.reset()
        PlaySound('sounds/ding.wav', SND_FILENAME)

    def dealCardOpen(self):
        p1 = PhotoImage(file="cards/" + self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image=p1)  # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image = p1  # 파이썬은 라벨이미지 레퍼런스를 갖고있어야 이미지가 보임

        p2 = PhotoImage(file="cards/" + self.dealer.cards[1].filename())
        self.LcardsDealer[1].configure(image=p2)  # 이미지 레퍼런스 변경
        self.LcardsDealer[1].image = p2  # 파이썬은 라벨이미지 레퍼런스를 갖고있어야 이미지가 보임

    def checkWinner(self):
        self.dealCardOpen()
        if self.Result(self.dealer)<self.Result(self.player):
            self.Lstatus.configure(text="Win!!")
            self.playerMoney += self.betMoney * 2
            PlaySound('sounds/win.wav', SND_FILENAME)

        elif self.Result(self.dealer)>self.Result(self.player):
            self.Lstatus.configure(text="Lose,,")
            PlaySound('sounds/wrong.wav', SND_FILENAME)

        elif self.Result(self.dealer)==self.Result(self.player):

            self.Lstatus.configure(text="Push")
            self.playerMoney += self.betMoney
            PlaySound('sounds/win.wav', SND_FILENAME)

        self.betMoney = 0
        self.LplayerMoney.configure(text="You have$" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))

    def Result(self,P):
        if (self.Four(P)):
            point=self.Four(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="Four" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="Four" + str(point))
            if point==1:
                point+=13
            return 700+point

        elif (self.FullHouse(P)):
            point=self.FullHouse(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="Full House" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="Full House" + str(point))
            if point==1:
                point+=13
            return 600+point

        elif (self.Flush(P)):
            point=self.Flush(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="Flush" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="Flush" + str(point))
            if point==1:
                point+=13
            return 500+point
        elif (self.Straight(P)):
            point=self.Straight(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="Straight" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="Straight" + str(point))
            if point==1:
                point+=13
            return 400+point
        elif (self.Triple(P)):
            point=self.Triple(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="Triple" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="Triple" + str(point))
            if point==1:
                point+=13
            return 300+point
        elif (self.TwoPair(P)):
            point=self.TwoPair(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="TwoPair" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="TwoPair" + str(point))
            if point==1:
                point+=13
            return 200+point
        elif (self.OnePair(P)):
            point=self.OnePair(P)
            if P==self.dealer:
                self.LdealerPts.configure(text="OnePair" + str(point))
            if P==self.player:
                self.LplayerPts.configure(text="OnePair" + str(point))
            if point==1:
                point+=13
            return 100+point

        point=self.NoPair(P)
        if P == self.dealer:
            self.LdealerPts.configure(text="No Pair" + str(point))
        if P == self.player:
            self.LplayerPts.configure(text="No Pair" + str(point))
        if point == 1:
            point += 13
        return point

    def NoPair(self,P):
        l = []
        for i in range(7):
            if P.cards[i].getValue() in l:
                l.append(-1)
            else:
                l.append(P.cards[i].getValue())
        if 1 in l:
            return 1
        return max(l)

    def Flush(self,P):
        shape = [0] * 4
        for i in range(7):
            if P.cards[i].getsuit() == "Clubs":
                shape[0] += 1
            elif P.cards[i].getsuit() == "Spades":
                shape[1] += 1
            elif P.cards[i].getsuit() == "Hearts":
                shape[2] += 1
            elif P.cards[i].getsuit() == "Diamonds":
                shape[3] += 1

        for i in range(4):
            if shape[i] >= 5: #같은모양이 5이상이면
                l = []
                for j in range(7):
                    if P.cards[j].getX() == i:
                        l.append(P.cards[j].getValue())
                if 1 in l:
                    return 1
                return max(l)
        return False

    def FullHouse(self,P):
        num=[0]*13
        for i in range (7):
            for j in range (13):
                if P.cards[i].getValue() == j+1:
                    num[j] += 1
        if 3 in num:
            if 2 in num:
                if num.index(3)==0:
                    return 1
                elif num.index(2)==0:
                    return 1
                else :
                    return self.big(num.index(3),num.index(2))+1
        return False

    def big(self,a,b):
        if a>b:
            return a
        return b

    def Straight(self,P):
        l=[]
        for i in range(7):
            if P.cards[i].getValue() in l:
                l.append(-1)
            else:
                l.append(P.cards[i].getValue())
        l.sort()

        for i in range(0, 3):
            n = 0
            while (n < 4):
                if l[i + n] == l[i + n + 1] - 1:
                    n+=1
                    if n==4:
                        return l[i]
                    continue
                else:
                    break
        return False

    def Four(self,P):
        num=[0]*13
        for i in range (7):
            for j in range (13):
                if P.cards[i].getValue() == j+1:
                    num[j] += 1
        if 4 in num:
            return num.index(4)+1
        return False

    def Triple(self,P):
        num=[0]*13
        for i in range (7):
            for j in range (13):
                if P.cards[i].getValue() == j+1:
                    num[j] += 1
        if 3 in num:
            return num.index(3)+1
        return False

    def TwoPair(self,P):
        num = [0] * 13
        for i in range(7):
            for j in range(13):
                if P.cards[i].getValue() == j + 1:
                    num[j] += 1
        n=0
        for i in num:
            if i==2:
                n+=1
        n2=[]
        if n>=2:
            for i in range(13):
                if num[i]==2:
                    n2.append(i)
            if 0 in n2:
                return 1
            return max(n2)+1

        return False

    def OnePair(self, P):
        num = [0] * 13
        for i in range(7):
            for j in range(13):
                if P.cards[i].getValue() == j + 1:
                    num[j] += 1
        for i in num:
            if i == 2:
                if num[0]==2:
                    return 1
                return num.index(2)+1
        return False

TexasHoldemPoker()
