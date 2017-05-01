import sys
# 출려방향 변경
print("Coming through stdout")
# stdout is saved
save_stdout = sys.stdout
fh = open("test.txt","w")
sys.stdout = fh
print("This line goes to test.txt")
# return to normal:
sys.stdout = save_stdout
fh.close()

save_stderr = sys.stderr
fh = open("errors.txt","w")
sys.stderr = fh
x = 10 / 0
# return to normal:
sys.stderr = save_stderr
fh.close()