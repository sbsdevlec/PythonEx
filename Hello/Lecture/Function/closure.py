def outer_func(): #1
    message = 'Hi' #3
    def inner_func(): #4
        print(message) #6
    return inner_func() #5

def outer_func2(): #1
    message = 'Hi' #3
    def inner_func(): #4
        print(message) #6
    return inner_func #5

outer_func() #2
outer_func2()()