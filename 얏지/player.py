
class Player:
    UPPER = 6 # upper catergory 6개
    LOWER = 7 # lower category 7개
    def __init__(self,name):
        self.name = name
        self.scores = [-1 for i in range(self.UPPER+self.LOWER)] # 13개 category 점수
        #13개 category 사용여부
        self.used = [False for i in range(self.UPPER+self.LOWER)]

    def setScore(self,score,index):
        #카테고리별 점수 기입 적절하지 않으면 0 기입
        self.scores[index]=score

    def setAtUsed(self,index):
        # 카테고리에 점수 적었으면
        if self.scores[index]>=0:
            self.used[index]=True
        return self.used[index]


    def getUpperScore(self):
        #상단 6개 카테고리 전부 적었으면 점수 다 합하기
        sum=0
        for i in range(self.UPPER):
            sum+=self.scores[i]
        self.upperScore=sum
        return self.upperScore

    def getLowerScore(self):
        # 하단 7개 카테고리 전부 적었으면 점수 다 합하기
        sum=0
        for i in range(self.LOWER):
            sum+=self.scores[self.UPPER+i]
        self.lowerScore=sum
        return self.lowerScore

    def getUsed(self):
        #used 가져오는 get set 함수
        pass
    def getTotalScore(self):
        #13개 카테고리 전부 사용했으면 토탈내기
        return self.lowerScore+self.upperScore

    def toString(self):
        #이름을 반환하는 함수
        return self.name
    def allLowerUsed(self):
        #lower category 7개 모두 사용되었는가 ? true false 반환
        for i in range(6,13,1):
            print(i, "-", self.used[i])
            if (self.used[i] == False):
                return False
        return True


    def allUpperUsed(self):
        #upper category 6개 모두 사용되었는가 ? true false 반환
        # upper scores, upper bonus 계산에 활용
        for i in range(self.UPPER):
            if (self.used[i] == False):
                return False
        return True