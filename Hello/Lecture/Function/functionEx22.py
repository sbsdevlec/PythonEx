def messageSum(message, *params):
    print(message, end=' : ')
    s = 0
    for i in params:
        s += i
    print(s)

messageSum("1~ 6까지 합계",1,2,3,4,5,6)
messageSum("1~ 10까지 합계",1,2,3,4,5,6,7,8,9,10)
l = [1,2,3,4,5,6,7,8,9,10]
messageSum("1~ 10까지 합계",*l)
t = (1,2,3,4,5,6,7,8,9,10)
messageSum("1~ 10까지 합계",*t)
