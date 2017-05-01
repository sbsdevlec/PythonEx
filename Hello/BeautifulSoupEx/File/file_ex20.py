import os
import tempfile

# tempfile을 사용하면 사용이 종료되면 자동으로 삭제가 됨
print( tempfile.gettempdir() )
t = tempfile.mkdtemp(dir='c:\\temp',prefix='test_')
print(t)
for i in range(10):
    tempfile.NamedTemporaryFile(prefix='test_',suffix='.temp', dir=t,delete=False)
    with tempfile.TemporaryFile('w+t', prefix='sample_', suffix='.txt', dir=t, delete=False) as f:
        f.write('한글은?\n')
        f.write('Testing\n')
        f.close()