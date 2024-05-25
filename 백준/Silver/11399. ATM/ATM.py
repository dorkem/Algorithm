import sys
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().split()))
b.sort()
c = 0

for i in range(len(b)+1):
  c += sum(b[:i])
print(c)