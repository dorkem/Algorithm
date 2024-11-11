import math

i, j = map(int,input().split())
n, m = map(int,input().split())

mother = j*m // math.gcd(j,m)
son = (mother//j)*i + (mother//m)*n

l = math.gcd(mother, son)
mother //= l
son //= l

print(son, mother)