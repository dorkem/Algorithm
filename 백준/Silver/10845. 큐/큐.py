import sys

a = int(sys.stdin.readline())
q = []
for _ in range(a):
  b = sys.stdin.readline().strip().split()
  if b[0] == "push":
    q.append(b[1])
  elif b[0] == "pop":
    if q:
        print(q.pop(0))
    else:
        print("-1")
  elif b[0] == "front":
    if q:
      print(q[0])
    else:
      print("-1")
  elif b[0] == "back":
    if q:
      print(q[-1])
    else:
      print("-1")
  elif b[0] == "empty":
    if q:
      print(0)
    else:
      print(1)
  else:
    print(len(q))
