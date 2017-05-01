height = int(input("몇줄짜리?"))
str=""
for i in range(1,height+1):
    str += "  "*(height-i) + "☆"*(i*2-1) + "\n"

for i in range(height,0,-1):
    str += "  "*(height-i) + "☆"*(i*2-1) + "\n"

for i in range(1,height+1):
    str += "  " * (height - i) + "☆" * (i * 2 - 1) + "\n"
for i in range(height-1,0,-1):
    str += "  " * (height - i) + "☆" * (i * 2 - 1) + "\n"

len = 0
for i in range(1,height*2):
    if i<=height:
        len += 1
    else:
        len -= 1
    str += "  " * (height - len) + "☆" * (len * 2 - 1) + "\n"

print(str)


