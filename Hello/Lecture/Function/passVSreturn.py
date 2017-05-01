def passFunction():
    print("난 어떻게 되나요?") # 실행됨
    pass # 아무것도 수행하지 않는다~~
    print("또다른 나는 어떻게 되나요?") # 실행됨

def returnFunction():
    print("난 어떻게 되나요?") # 실행됨
    return
    print("또다른 나는 어떻게 되나요?")  # 실행됨

passFunction()
returnFunction()
