import sys

input = sys.stdin.readline

a, b = map(int, input().split())
pocket = {}

for i in range(1, a + 1):
  name = input().rstrip()  #\n문자제거
  pocket[i] = name
  pocket[name] = i

for _ in range(b):
  q = input().rstrip()
  if q.isdigit():
    print(pocket[int(q)])
  else:
    print(pocket[q])
