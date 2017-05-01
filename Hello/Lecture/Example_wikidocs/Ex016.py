"""
016 문자열 거꾸로 뒤집기
문자열을 거꾸로 뒤집어 출력하라.
string = "파이선은 재미있다."
실행 예:
'NOHTYP'
"""
string = "파이선은 재미있다."
print(string)
# string[start:stop:step]
print(string[::-1])
# print(string[:-1])

print(type(reversed(string)))
print(reversed(string))
print(''.join(reversed(string)))

"""
여러분이 알아야 할 파이썬 문자열에 관한 몇 가지 것들이 있습니다 :
파이썬에서는 문자열이 변경되지 않습니다 . 문자열을 변경해도 문자열은 수정되지 않습니다. 새로운 것을 만듭니다.
문자열은 슬라이스 가능합니다. 문자열을 자르는 것은 문자열의 한 지점에서 앞으로 또는 앞으로 다른 지점으로 주어진 
증가분만큼 새로운 문자열을 제공합니다. 그들은 아래 첨자에 슬라이스 표기법 또는 슬라이스 객체를 사용합니다.

string[start:stop:step]

중괄호 밖에서 슬라이스를 만들려면 슬라이스 객체를 만들어야합니다.
slice_obj = slice(start, stop, step)
string[slice_obj]
"""

# 슬라이스객체 사용
start = stop = None
step = -1
reverse_slice = slice(start, stop, step)
print(string[reverse_slice])

# 슬라이스객체 사용
slice_obj = slice(None, None, -1)
print(string[slice_obj])

# 1줄
print("파이선은 재미있다."[::-1])

# 함수이용
def reversed_string(a_string):
    return a_string[::-1]

print(reversed_string(string))

# 선생님이 원했던 것
def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1                    # index = index - 1
        new_string += a_string[index] # new_string = new_string + character
    return new_string

print(reverse_a_string_slowly(string))

"""
참조
"""
### example02 -------------------
## start (with positive integers)
print('coup_ate_grouping'[0]) ## => 'c'
print('coup_ate_grouping'[1]) ## => 'o' 
print('coup_ate_grouping'[2]) ## => 'u' 

## start (with negative integers)
print('coup_ate_grouping'[-1]) ## => 'g'
print('coup_ate_grouping'[-2]) ## => 'n' 
print('coup_ate_grouping'[-3]) ## => 'i' 

## start:end 
print('coup_ate_grouping'[0:4])   ## => 'coup'    
print('coup_ate_grouping'[4:8])   ## => '_ate'    
print('coup_ate_grouping'[8:12])  ## => '_gro'    

## start:end 
print('coup_ate_grouping'[-4:])   ## => 'ping' (counter-intuitive)
print('coup_ate_grouping'[-4:-1]) ## => 'pin'
print('coup_ate_grouping'[-4:-2]) ## => 'pi'
print('coup_ate_grouping'[-4:-3]) ## => 'p'
print('coup_ate_grouping'[-4:-4]) ## => ''
print('coup_ate_grouping'[0:-1])  ## => 'coup_ate_groupin'
print('coup_ate_grouping'[0:])    ## => 'coup_ate_grouping' (counter-intuitive)

## start:end:step (or stop:end:stride)
print('coup_ate_grouping'[-1:]) ## => 'g'
print('coup_ate_grouping'[-1::1]) ## => 'g'
print('coup_ate_grouping'[-1::-1])## => 'gnipuorg_eta_puoc'

## combinations
print('coup_ate_grouping'[-1::-1][-4:])## => 'puoc'