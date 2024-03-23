import sys

stack = []
a = int(sys.stdin.readline())

for _ in range(a):
  b = sys.stdin.readline().split()
  if b[0] == '1':
    stack.append(b[1])
  elif b[0] == '2':
    if stack:
      print(stack.pop())
    else:
      print(-1)
  elif b[0] == '3':
    print(len(stack))
  elif b[0] == '4':
    if stack:
      print(0)
    else:
      print(1)
  elif b[0] == '5':
    if stack:
      print(stack[-1])
    else:
      print(-1)
