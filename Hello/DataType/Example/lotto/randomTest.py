import random as rnd

print(rnd.random())                 # Random float:  0.0 <= x < 1.0
print(rnd.uniform(2.5, 10.0))       # Random float:  2.5 <= x < 10.0

# random.randrange(stop)
# random.randrange(start, stop[, step])
print(rnd.randrange(10))            # Integer from 0 to 9 inclusive
print(rnd.randrange(1,10))          # Integer from 1 to 9 inclusive
print(rnd.randrange(0, 101, 2))     # 2의배수(짝수)
print(rnd.randrange(1, 101, 2))     # 2의배수(홀수)
print(rnd.randrange(0, 101, 3))     # 3의배수
print(rnd.randrange(0, 101, 5))     # 5의베수


print(rnd.choice('일 이 삼 사 오 육 칠 팔 구 십'.split()))     # 1개 선택
print(rnd.choice('일이삼사오육칠팔구십'))     # 1개 선택
print(rnd.choice('1234567890'));

deck = '일 이 삼 사 오 육 칠 팔 구 십'.split()
print(deck)
rnd.shuffle(deck)
print(deck)
rnd.shuffle(deck)
print(deck)

print(rnd.sample([10, 20, 30, 40, 50], 4))

print(rnd.sample(range(1,46), 6))
lotto = rnd.sample(range(1,46), 6)
lotto.sort()
print(lotto)




