
age = int(input('나이는?'))
print("들어오세여" if age>=20 else "애들은 가라~~")

num = int(input('양의 정수?'))
print("홀수" if num%2 else "짝수")
print("홀수" if num%2==1 else "짝수")
print()
print("짝수" if num%2==0 else "홀수")
print("짝수" if num%2!=1 else "홀수")

year = int(input('년도?'))
print("윤년" if year%400==0 or year%4==0 and year%100!=0 else "평년")
print("윤년" if not year%400 or not year%4 and year%100 else "평년")
