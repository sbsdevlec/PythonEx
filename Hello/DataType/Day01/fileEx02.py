height = int(input("몇줄짜리?"))

for i in range(1,height+1):
    print("  "*(height-i), end="")
    print("☆"*(i*2-1))
print()