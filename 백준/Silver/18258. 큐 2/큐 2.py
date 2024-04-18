import sys
from collections import deque

input = sys.stdin.readline
q = deque([])

a = int(input())

for _ in range(a):
  b = input().split()
  if b[0] == "push":
    q.append(b[1])
  elif b[0] == "pop":
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif b[0] == "size":
    print(len(q))
  elif b[0] == "empty":
    if not q:
      print(1)
    else:
      print(0)
  elif b[0] == "front":
    if q:
      print(q[0])
    else:
      print(-1)
  elif b[0] == "back":
    if q:
      print(q[-1])
    else:
      print(-1)