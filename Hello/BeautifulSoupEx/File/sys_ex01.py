import sys
# 파이선 정보 확인
print('Version info:')
print()
print('sys.version      =', repr(sys.version))
print('sys.version_info =', sys.version_info)
print('sys.hexversion   =', hex(sys.hexversion))
print('sys.api_version  =', sys.api_version)
print()

# Install Location
print('This interpreter was built for:', sys.platform)
print('Interpreter executable:', sys.executable)
print('Installation prefix   :', sys.prefix)
print()

# Unicode Defaults
print('Default encoding    :', sys.getdefaultencoding())
print('Filesystem encoding :', sys.getfilesystemencoding())
print()

# Command Line Options
print(sys.flags)
print()

# Interactive Prompts
"""
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>>

>>> sys.ps1 = '::: '
::: sys.ps2 = '~~~ '
::: for i in range(3):
~~~   print i
~~~
0
1
2
:::
"""
