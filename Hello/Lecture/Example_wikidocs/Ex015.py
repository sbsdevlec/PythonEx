"""
015 문자열 분리
영상의 크기를 resolution이 바이딩하고 있을 때 영상의 너비와 높이를 출력하라. 예를 들어, "176x144"이면 너비가 176 높이가 144이다.
resolution2 = '1920x1080'
width: 1920
height: 1080
"""
resolution2 = '1920x1080'
print("폭 : ", resolution2[0:4])
print("높이 : ", resolution2[5:])

resolution = resolution2.split("x")
print(type(resolution))
print("폭 : ", resolution[0])
print("높이 : ", resolution[1])


