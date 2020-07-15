from dice import*

class Configuration:

    configs = ["Category","Ones","Twos","Threes","Fours","Fives","Sixes",
        "Upper Scores","Upper Bonus(35)","Three of a kind","Four of a kind","Full House(25)",
        "Small Straight(30)","Large Straight(40)","Yahtzee(50)","Chance","Lower Scores","Total"]

    def getConfigs(self): # 정적 메소드 : 객체생성 없이 사용가능
        #config 반환하는거. 근데 쓰이지 않음
        return Configuration.configs

    def score(row,d): # 정적 메소드 : 객체생성 없이 사용가능
        #row에 따라 주사위 점수를 계산 반환,예를 들어 row가 0이면 "Ones"가 채점되어야 함을
        #의미합니다. row가 2이면 ,Threes가 득점되어야 함을 의미, row가 득점(scored)하지
        #않아야 하는 버튼(즉,UpperScore,UpperBonus,LowerScore,Total 등)을 나타내는 경우
        #-1 을 반환합니다.
        if(row>=0 and row<=5):
            return Configuration.scoreUpper(d,row+1)
        elif(row==8):
            return Configuration.scoreThreeOfAKind(d)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(d)
        elif (row == 10):
            return Configuration.scoreFullHouse(d)
        elif (row ==11):
            return Configuration.scoreSmallStraight(d)
        elif (row == 12):
            return Configuration.scoreLargeStraight(d)
        elif (row == 13):
            return Configuration.scoreYahtzee(d)
        elif (row == 14):
            return Configuration.sumDie(d)
        else: #UPPER TOTAL, UPPER BONUS, LOWER TOTAL,TOTAL
            return -1

    def scoreUpper(d, num):  # 정적 메소드 : 객체생성 없이 사용가능
        # Upper Section 구성(Ones,Twos,Threes,...)에 대해 주사위 점수를 매깁니다.
        # 예를 들어, num이 1이면 "Ones"구성의 주사위 점수를 반홥합니다.
        s = 0
        for i in range(5):
            if (d[i].getRoll() == num):
                s += num
        return s

    def scoreThreeOfAKind(d):  # 모든 주사위의 합계
         freg=[0]*6
         for i in range(5):
             freg[d[i].getRoll()-1]+=1
         if max(freg)>=3:
                 return Configuration.sumDie(d)
         else:
             return 0

    def scoreFourOfAKind(d):  # 모든 주사위의 합계
        freg = [0] * 6
        for i in range(5):
            freg[d[i].getRoll() - 1] += 1
        if max(freg)>=4:
                return Configuration.sumDie(d)
        else:
            return 0

    def scoreFullHouse(d):  # 25점
        freg = [0] * 6
        for i in range(5):
            freg[d[i].getRoll() - 1] += 1
        freg.sort()
        if freg[5]==3 and freg[4]==2:
            return 25
        else:
            return 0

    def scoreSmallStraight(d):  # 30점
        # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
        die=[0]*5
        dice=[]
        for i in range(5):
            die[i] = d[i].getRoll()
        for i in die:
            if not i in dice:
                dice.append(i)
        dice.sort()
        if dice==[1,2,3,4] or dice==[2,3,4,5]or dice==[3,4,5,6] or dice==[1,2,3,4,5] or dice==[2,3,4,5,6]:
                return 30
        else:
            return 0

    def scoreLargeStraight(d):  # 40점
        # 1 2 3 4 5 혹은 2 3 4 5 6 검사
        die = [0] * 5
        for i in range(5):
            die[i] = d[i].getRoll()
        die.sort()
        if die==[1,2,3,4,5] or die==[2,3,4,5,6]:
            return 40
        else:
            return 0

    def scoreYahtzee(d):  # 50점
        if d[0].getRoll()==d[1].getRoll()==d[2].getRoll()==d[3].getRoll()==d[4].getRoll():
            return 50
        else:
            return 0

    def sumDie(d):  # 5개의 주사위 합
        s=0
        for i in range(5):
            s+=d[i].getRoll()
        return s

