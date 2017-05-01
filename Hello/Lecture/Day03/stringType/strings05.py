str="안녕하세요"
print("'{0}'".format(str))
print("'{0:30}'".format(str))   # 길이
print("'{0:<30}'".format(str))  # 왼쪽정렬
print("'{0:>30}'".format(str))  # 오른쪽정렬
print("'{0:^30}'".format(str))  # 중앙정렬
print("'{0:*^30}'".format(str))  # 중앙정렬 공백채우기
print("'{0:~<30}'".format(str))  # 왼쪽정렬 공백채우기
print("'{0:^>30}'".format(str))  # 오른쪽정렬 공백채우기
print("'{0:.1}'".format(str))    # 자르기
print("'{0:.2}'".format(str))    # 자르기
print("'{0:.3}'".format(str))    # 자르기
print("'{0:10.3}'".format(str))    # 자르기
print()

print("{0:10d}{1:10d}{2:10d}".format(1,2,3))
print("{0:10d}{1:10d}{2:10d}".format(11,22,33))
print("{0:10d}{1:10d}{2:10d}".format(111,222,333))
print("{0:+10d}{1:+10d}{2:+10d}".format(111,222,-333)) # +
print("{0:=10d}{1:=10d}{2:=10d}".format(111,222,-333)) # =
print("{0:=+10d}{1:=+10d}{2:=+10d}".format(111,222,-333)) # =+
print("{0:<10d}{1:<10d}{2:<10d}".format(111,222,333))
print()

print("{0:.3f} {1:.3f} {2:.3f}".format(1.1,2.34,5.6789))
print("{0:10.3f} {1:10.3f} {2:10.3f}".format(1.1,2.34,5.6789))
print('{:f}'.format(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
print()


