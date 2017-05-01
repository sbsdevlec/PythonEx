def counter1():
    counter = 0
    counter += 1
    print("호출 횟수 : ", counter)

def counter2():
    counter2.counter += 1
    print("호출 횟수 : ", counter2.counter)
counter2.counter = 0

def counter3():
    try:
        counter3.counter += 1
    except AttributeError:
        counter3.counter = 1
    print("호출 횟수 : ", counter3.counter)

def static_var(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate

@static_var('counter', 0)
def counter4():
    counter4.counter += 1
    print("호출 횟수 : ", counter4.counter)

def counter5(counter=[0]):
    counter[0] += 1
    print("호출 횟수 : ", counter[0])

def counter6(static={'counter':0}):
    static['counter'] += 1
    print("호출 횟수 : ", static['counter'] )

counter1()
counter1()
counter1()
print(vars(counter1))
print()

counter2()
counter2()
counter2()
counter2.counter = 5
print(counter2.counter)
counter2()
print(vars(counter2))
print()

counter3()
counter3()
counter3()
counter3.counter = 5
print(counter3.counter)
counter3()
print(vars(counter3))
print()

print(vars(counter4))
counter4()
counter4()
counter4()
counter4.counter=100
print(counter4.counter)
counter4()
print(vars(counter4))
print()

print(vars(counter5))
counter5()
counter5()
counter5()
counter5.counter=100
print(counter5.counter)
counter5()
print(vars(counter5))
print()

print(vars(counter6))
counter6()
counter6()
counter6()
counter6.staic=100
print(counter6.staic)
counter6()
print(vars(counter6))
print()
