a = int(input())
for i in range(a):
  stack = []
  b=input()
  for j in range(len(b)):
    if b[j] == '(':
      stack.append(b[j])
    elif b[j] == ')':
      if not stack:
        stack.append(b[j])
        break
      else:
        stack.pop()
  if stack:
    print('NO')
  elif not stack:
    print('YES')