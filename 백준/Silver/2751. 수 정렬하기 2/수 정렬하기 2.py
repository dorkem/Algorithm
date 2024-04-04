import sys
a = int(sys.stdin.readline())
c = []
for i in range(a):
  b = int(sys.stdin.readline())
  c.append(b)

c = sorted(c)

for i in range(a):
  print(c[i])