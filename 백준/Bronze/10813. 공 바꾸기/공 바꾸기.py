a, b = map(int,input().split())
c = list(range(1, a+1))

for i in range(b):
    d, e = map(int,input().split())
    c[d-1],c[e-1]=c[e-1],c[d-1]

for i in range(a):
  print(c[i], end=' ')