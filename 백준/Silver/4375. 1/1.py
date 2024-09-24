import sys

for line in sys.stdin:
    num = int(line.strip()) 
    count = 1
    len = 1
    while 1:
        if count % num == 0:
            print(len)
            break
        count = count * 10 + 1
        len+=1