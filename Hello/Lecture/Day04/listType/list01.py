list0 =[]
print(list0)
print(type(list0))

list1 = [1,2,3,4,5,6,7,8,9,0]
print(list1)

list2 = ['1','2','3','4']
print(list2)

list3 = ['1','2',3,4]
print(list3)

for i in list3:
    print(i)

for i in range(len(list3)):
    print(i, list3[i])
print()

list4 = [[1,2,3],[1,2,3,4,5,6],["하나","두울","세엣"]]
print(len(list4))
print(len(list4[1]))
for i in range(len(list4)):
    for j in range(len(list4[i])):
        print(i,j, list4[i][j])
    print()
