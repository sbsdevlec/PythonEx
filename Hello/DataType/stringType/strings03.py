# 이전 방식의 문자열 형식
name="한사람"
age=34
gender=True
height = 178.7

"""
코드	설명
%s	문자열 (String)
%c	문자 1개(character)
%d	정수 (Integer)
%f	부동소수 (floating-point)
%o	8진수
%x	16진수
%%	% 출력
"""

print("%s님의 나이는 %d세입니다."%(name,age))
print("%s님의 성별은 '%s'입니다."%(name, "남자" if gender else "여자"))
print("%s님의 성별은 '%c'입니다."%(name, "M" if gender else "F"))
print("%s님의 성별은 \"%s\"입니다."%(name, "남자" if gender else "여자"))
print("%s님은 \"%s\"입니다."%(name, "성년" if age>20 else "미성년"))
print("%s님의 신장은 %.2fCm입니다."%(name,height))
print("%s님의 상위 %d%%에 속하는 사람입니다."%(name,5))
print("%d %x %o"%(100,100,100))

