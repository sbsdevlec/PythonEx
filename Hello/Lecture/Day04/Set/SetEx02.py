"""
Set의 연산
수학에서 두개의 집합 간의 연산으로 교집합, 합집합, 차집합이 있는데, set 클래스는 이러한 집합 연산 기능을 제공한다. 
즉, a와 b가 set 일 때, 교집합은 a & b (혹은 a.intersection(b)), 합집합은 a | b (혹은 a.union(b)), 차집합은 a - b (혹은 a.differene) 와 같이 구할 수 있다.
"""
set1 = {1,3,5,7,9}
set2 = {1,2,3,4,5}
print(set1)
print(set2)
# 교집합
set3 = set1 & set2
print(set3)

# 합집합
set4 = set1 | set2
print(set4)

# 차집합
set5 = set1 - set2
print(set5)
set5 = set2 - set1
print(set5)
