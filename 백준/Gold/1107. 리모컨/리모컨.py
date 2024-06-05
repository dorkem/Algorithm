import sys
input = sys.stdin.readline
num = int(input())
pung = int(input())
no = list(map(int,input().split()))

n = abs(100 - num)

for i in range(1000000):
    i = str(i) #일단 졸라눌러
    for j in range(len(i)):
        if int(i[j]) in no: #고장난 버튼이 포함되면 무시
            break
        elif j == len(i) - 1: 
            n = min(n, abs(int(i) - num) + len(i))
print(n)
            