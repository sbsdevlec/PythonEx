height = int(input("몇줄짜리?"))
for i in range(1,height+1):
    print("☆"*i)
print()

for i in range(height,0,-1):
    print("☆"*i)
print()

for i in range(1,height+1):
    print("☆"*i)
for i in range(height-1,0,-1):
    print("☆"*i)
print()

len = 0
for i in range(1,height*2):
    if i<=height:
        len += 1
    else:
        len -= 1
    print("☆"*len)
print()

