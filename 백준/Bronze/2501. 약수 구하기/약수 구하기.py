a, b = map(int, input().split())
list = []

for i in range(a):
  d = (a - i)
  c = a % d
  if c == 0:
    list.append(d)

if len(list)<b:
  print(0)
else :
  print(list[-b])