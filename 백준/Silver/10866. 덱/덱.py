from collections import deque
import sys
a = int(sys.stdin.readline())
Deque = deque([])
for _ in range(a):
  b = list(sys.stdin.readline().strip().split())
  if b[0] == "push_front":
    Deque.appendleft(b[1])
  elif b[0] == "push_back":
    Deque.append(b[1])
  elif b[0] == "front":
    if Deque:
      print(Deque[0])
    else:
      print(-1)
  elif b[0] == "back":
    if Deque:
      print(Deque[-1])
    else:
      print(-1)
  elif b[0] == "pop_front":
    if Deque:
      print(Deque.popleft())
    else:
      print(-1)
  elif b[0] == "pop_back":
    if Deque:
      print(Deque.pop())
    else:
      print(-1)
  elif b[0] == "size":
    print(len(Deque))
  else:
    if Deque:
      print(0)
    else:
      print(1)