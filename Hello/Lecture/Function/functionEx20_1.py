def counter1():
    counter = 0
    counter += 1
    print("호출 횟수 : ", counter)

counter1()
counter1()
counter1()
print(vars(counter1))
print()
