import random

def lottoGame():
    lotto = random.sample(range(1,46),6)
    lotto.sort()
    return lotto

gameCount = int(input("몇게임할래?"))
for i in range(1,gameCount+1):
    print(i, lottoGame())



