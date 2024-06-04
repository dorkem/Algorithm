k = int(input())
stack = []
pm = []
big = 1
hi = True
for i in range(k):
  a = int(input())
  #처음 나온 숫자만큼 append함
  #그다음 숫자가 바로 아래 숫자면pop,
  #더 아래 숫자면 No출력후 리턴
  #높은숫자면 현재꺼 팝하고 반복해서 스택에 쌓기
  if i == 0:
    big = a
    for i in range(1, a + 1):
      stack.append(i)
      pm.append("+")
    stack.pop()
    pm.append("-")
  else:
    if a > big:
      for _ in range(a - big):
        big += 1
        stack.append(big)
        pm.append("+")
      stack.pop()
      pm.append("-")
    elif stack[-1] == a:
      stack.pop()
      pm.append("-")
    else:
      hi = False
      break
if hi==True:
  for i in pm:
    print(i)
else:
  print("NO")