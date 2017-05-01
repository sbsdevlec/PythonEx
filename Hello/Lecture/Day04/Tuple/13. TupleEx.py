# Python Tuple Methods
my_tuple = ('a','p','p','l','e',)

# Count : x 와 같은 항목의 수를 반환합니다.
# Output: 2
print(my_tuple.count('p'))

# Index : x 와 같은 첫 번째 항목의 인덱스를 반환합니다.
# Output: 3
print(my_tuple.index('l'))
my_tuple = tuple("qwertyqwertyqwerty")
print(my_tuple)
print(my_tuple.index('q'))
print(my_tuple.index('q',my_tuple.index('q')+1))
print(my_tuple.index('q',my_tuple.index('q',my_tuple.index('q')+1)+1))