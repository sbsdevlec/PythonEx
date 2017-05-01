import random

print(random.sample(range(1,46),6))
lotto = random.sample(range(1,46),6)
print(type(lotto))
print(lotto)
lotto.sort()
print(lotto)
