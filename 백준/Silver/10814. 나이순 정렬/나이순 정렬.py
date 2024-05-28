import sys
input = sys.stdin.readline
lst = []
a = int(input())
for _ in range(a):
    a, b = input().split()
    lst.append([int(a),b])

lst.sort(key = lambda x: (x[0]))

for i in lst:
    print(i[0], i[1])