import random

def lottoGame():
    lotto = set()
    while len(lotto) < 6:
        lotto.add(random.randrange(1, 46))
    s = list(lotto)
    s.sort()
    return s

gameCount = int(input("몇게임할래?"))
for i in range(1,gameCount+1):
    print(i, lottoGame())



