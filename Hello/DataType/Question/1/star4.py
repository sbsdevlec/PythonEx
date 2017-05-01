height = int(input("몇줄짜리?"))

for i in range(1,height+1):
    print("  "*(height-i),"☆"*(i*2-1),sep="")
print()

for i in range(height,0,-1):
    print("  "*(height-i),"☆"*(i*2-1),sep="")
print()

for i in range(1,height+1):
    print("  " * (height - i), "☆" * (i * 2 - 1), sep="")
for i in range(height-1,0,-1):
    print("  " * (height - i), "☆" * (i * 2 - 1), sep="")
print()

len = 0
for i in range(1,height*2):
    if i<=height:
        len += 1
    else:
        len -= 1
    print("  " * (height - len), "☆" * (len * 2 - 1),sep="")
print()
