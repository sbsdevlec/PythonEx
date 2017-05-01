import random

def lottoGame():
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return lotto

gameCount = int(input("몇게임할래?"))
while gameCount>0:
    print(lottoGame())
    gameCount-=1



