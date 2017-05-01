import random
def computer_random():
    lotto = random.sample(range(1,46), 6)
    return lotto

lotto = computer_random();
print(type(lotto))
lotto.sort()
print(lotto)
