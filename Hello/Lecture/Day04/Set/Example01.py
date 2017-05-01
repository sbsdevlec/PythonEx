import random
lotto = set()
print(lotto)
print(len(lotto))

while len(lotto)<6:
    lotto.add(random.randrange(1,46))

print(lotto)
list = list(lotto)
list.sort()
print(list)

print(random.sample(range(1,46),6))
lotto2 = random.sample(range(1,46),6)
print(type(lotto2))
lotto2.sort()
print(lotto2)