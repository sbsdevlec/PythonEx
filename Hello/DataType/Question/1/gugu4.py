
print("-"*80)
for i in range(1,10): print("{0:4d}단  ".format(i), end=" ")
print()
print("-"*80)
for i in range(1,10):
    for j in range(1,10):
        print("{0:3d}*{1:1d}={2:2d}".format(j,i,i*j), end=" ")
    print()
print("-"*80)
