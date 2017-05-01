num = 100
print("원본 : ", num)
print(bin(num))
# 10진수 -> 2진수 변환
print(oct(num))
# 10진수 -> 8진수 변환
print(hex(num))
# 10진수 -> 16진수 변환
print(int(bin(num),2))
# 2진수 -> 10진수 변환
print(int(oct(num),8))
# 8진수 -> 10진수 변환
print(int(hex(num),16))
# 16진수 -> 10진수 변환
print("-" * 40)

num = 0o100
print("원본 : ", num)
print(bin(num))
print(oct(num))
print(hex(num))
print(int(bin(num),2))
print(int(oct(num),8))
print(int(hex(num),16))
print("-" * 40)

num = 0x100
print("원본 : " , num)
print(bin(num))
print(oct(num))
print(hex(num))
print(int(bin(num),2))
print(int(oct(num),8))
print(int(hex(num),16))
print("-" * 40)

num = 0b10010011
print("원본 : " , num)
print(bin(num))
print(oct(num))
print(hex(num))
print(int(bin(num),2))
print(int(oct(num),8))
print(int(hex(num),16))
print("-" * 40)
