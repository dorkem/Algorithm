import sys

a = int(sys.stdin.readline())
s = []
for _ in range(a):
  b = sys.stdin.readline().strip().split()
  if b[0] == "push":
    s.append(b[1])
  elif b[0] == "pop":
    if s:
        print(s.pop())
    else:
        print("-1")
  elif b[0] == "top":
    if s:
      print(s[-1])
    else:
      print("-1")
  elif b[0] == "empty":
    if s:
      print(0)
    else:
      print(1)
  else:
    print(len(s))
