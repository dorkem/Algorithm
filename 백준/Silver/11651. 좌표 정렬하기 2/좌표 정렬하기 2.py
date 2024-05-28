import sys
input = sys.stdin.readline
lst = []
a = int(input())
for _ in range(a):
    a, b = map(int, input().split())
    lst.append([a,b])

lst.sort(key = lambda x: (x[1], x[0]))

for i in lst:
    print(i[0], i[1])