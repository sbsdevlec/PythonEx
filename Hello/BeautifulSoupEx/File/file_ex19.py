import os
from tempfile import TemporaryFile

# tempfile을 사용하면 사용이 종료되면 자동으로 삭제가 됨

with TemporaryFile('w+t') as f:
    print(f.name)
    f.write('한글은?\n')
    f.write('Testing\n')
    print(f.encoding)
    f.seek(0)
    data = f.read()
    print(data)
print()

with TemporaryFile('w+t',prefix='sample_',suffix='_temp',encoding='utf-8') as f:
    print(f.name)
    f.write('한글은?\n')
    f.write('Testing\n')
    print(f.encoding)
    f.seek(0)
    data = f.read()
    print(data)
