
print("-"*190)
for i in range(1,20): print("{0:5d}단  ".format(i), end=" ")
print()
print("-"*190)
for i in range(1,20):
    for j in range(1,20):
        print("{0:2d}*{1:2d}={2:3d}".format(j,i,i*j), end=" ")
    print()
print("-"*190)
