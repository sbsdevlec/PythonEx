# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
from builtins import print

print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

my_tuple = ('p','r','o','g','r','a','m','i','z')

# Deleting a Tuple
# can't delete items
# if you uncomment line 8,
# you will get an error:
# TypeError: 'tuple' object doesn't support item deletion

#del my_tuple[3]

# can delete entire tuple
# NameError: name 'my_tuple' is not defined
del my_tuple
print(my_tuple)
"""
Traceback (most recent call last):
  File "C:/Users/DJA/PycharmProjects/Lecture/Day03/Tuple/12. TupleEx.py", line 24, in <module>
    print(my_tuple)
NameError: name 'my_tuple' is not defined
"""