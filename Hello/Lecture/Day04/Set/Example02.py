import random
card = list(range(0,52))
print(card)
random.shuffle(card)
print(card)
cardName = ["◆","♠","♥","♣"]
cardNumber="1,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
print(cardName)
print(cardNumber)
cnt=0;
for i in card:
    cnt += 1
    print("{0:2d}:{1:1s}{2:2s}".format(i,cardName[i//13],cardNumber[i%13]),end= " ")
    if cnt%13==0: print()

