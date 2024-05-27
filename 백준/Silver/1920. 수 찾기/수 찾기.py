import sys
input = sys.stdin.readline
print = sys.stdout.write
a = int(input())
b = set(input().split())
c = int(input())
d = list(input().split())
for i in range(c):
    if d[i] in b:
        print("1\n")
    else:
        print("0\n")