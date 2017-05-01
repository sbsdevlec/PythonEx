"""
다음과 같이 출력되는 프로그램을 작성하라.(공백으로 구분하여 출력)
몇단?7
7단
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
"""
dan = int(input("몇단?"))
print(str(dan) + "단")
print("{0} * {1} = {2:3d}".format(dan,1,dan*1))

for i in range(2,10):
    print("{0} * {1} = {2:3d}".format(dan,i,dan*i))

print()

for i in range(1,10):
    print("%1d * %1d = %3d"%(dan,i,dan*i))
