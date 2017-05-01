height = int(input("몇줄짜리?"))
for i in range(1,height+1):
    print("  "*(height-i), end=" ")
    print("☆"*i)
print()
for i in range(1,height+1):
    print("  "*(i-1), end=" ")
    print("☆"*(height+1-i))
print()

for i in range(1,height+1):
    print("  "*(height-i), end=" ")
    print("☆"*i)
for i in range(2,height+1):
    print("  "*(i-1), end=" ")
    print("☆"*(height+1-i))
print()

len = 0
for i in range(1,height*2):
    if i<=height:
        len += 1
    else:
        len -= 1
    print("  " * (height - len), end=" ")
    print("☆"*len)
print()
len = 0
for i in range(1,height*2):
    len += 1 if i<=height else -1
    print("  " * (height - len), end=" ")
    print("☆"*len)
print()
