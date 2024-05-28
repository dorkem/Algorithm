import sys
from collections import Counter
input = sys.stdin.readline
a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = list(map(int,input().split()))

cnt = Counter(b)

for i in range(c):
    if d[i] in cnt:
        print(cnt[d[i]], end=' ')
    else:
        print(0, end=' ')