from itertools import product

a, b = map(int, input().split())
a = [str(i) for i in range(1, a + 1)]

for e in list(product(a, repeat=b)):
  print(" ".join(e))