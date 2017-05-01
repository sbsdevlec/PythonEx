import glob
import os.path

dir_count = file_count = 0

def traverse(dir, depth):
    global dir_count, file_count
    for obj in glob.glob(dir + "/*"):
        if depth==0:
            prefix = "|--"
        else:
            prefix = "|  " * depth + "|--"
        if os.path.isdir(obj): # 디렉토리인 경우
            dir_count += 1
            print(prefix + os.path.basename(obj))
            traverse(obj, depth+1)
        elif os.path.isfile(obj): # 파일인 경우
            file_count += 1
            print(prefix + os.path.basename(obj))
        else:
            print(prefix + 'unknown object : ', obj)

if __name__ == '__main__':
    traverse('../..',0)
    print('\n',dir_count,'directories',file_count,'files')
