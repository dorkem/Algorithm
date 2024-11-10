xar = []
yar = []
for _ in range(3):
   x, y = map(int, input().split())
   xar.append(x)
   yar.append(y)

for x in xar:
   if xar.count(x) == 1:
      n = x
      break
for y in yar:
   if yar.count(y) == 1:
      m = y
      break

print(n, m)