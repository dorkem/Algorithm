from itertools import combinations_with_replacement

a, b = map(int, input().split())
a = [str(i) for i in range(1, a + 1)]

for e in combinations_with_replacement(a, b):
    print(" ".join(e))
