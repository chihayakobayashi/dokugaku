class Bingo:

    card1 = []
    card2 = []
    card3 = []

    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def card(self):
        import random
        self.a = random.randint(1,99)
        self.b = random.randint(1,99)
        self.c = random.randint(1,99)
        self.d = random.randint(1,99)
        self.e = random.randint(1,99)
        self.f = random.randint(1,99)
        self.g = random.randint(1,99)
        self.h = random.randint(1,99)
        self.i = random.randint(1,99)

        self.card1.append(self.a)
        self.card1.append(self.b)
        self.card1.append(self.c)
        self.card2.append(self.d)
        self.card2.append(self.e)
        self.card2.append(self.f)
        self.card3.append(self.g)
        self.card3.append(self.h)
        self.card3.append(self.i)

        print("あなたのカードはこちらです")
        print(self.card1)
        print(self.card2)
        print(self.card3)

def search(x,y):
    if x in y:
        where = y.index(x)
        y[where] = 0

def ender(card1,card2,card3):
    if not ((any(card1) == True) and (any(card2) == True) and (any(card3) == True)):
        return True

    for i in range(0,3):
        if card1[i] == 0 and card2[i] == 0 and card3[i] == 0:
            return True

    if card1[0] == 0 and card2[1] == 0 and card3[2] == 0:
        return True
    if card1[2] == 0 and card2[1] == 0 and card3[0] == 0:
        return True
    return False

def game():
    bingo = Bingo(1,2,3,4,5,6,7,8,9)
    bingo.card()
    count = 0
    balls = []
    for i in range (1,100):
        balls.append(i)
    print("\n")
    end = False
    while end is not True:
        count += 1
        print("{}回目の挑戦!".format(count))
        start = input("q以外のキーで実行、qで中止")
        if start == "q":
            break
        else:
            print("\n")
            import random
            ball = random.choice(balls)
            balls.remove(ball)
            print("{}が出ました".format(ball))
            search(ball,bingo.card1)
            search(ball,bingo.card2)
            search(ball,bingo.card3)
            print(bingo.card1)
            print(bingo.card2)
            print(bingo.card3)
            end = ender(bingo.card1,bingo.card2,bingo.card3)
            print("\n")
            
    print("ビンゴ!{}回目の挑戦でビンゴが出ました。".format(count))   



game()




















    
        
        
