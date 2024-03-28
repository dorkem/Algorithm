a, b = map(int, input().split())
c = []
ans = 0

for i in range(a):
  coin = int(input())
  c.append(coin)

c.sort(reverse=True)

i = 0

while (b != 0):
  if (c[i] > b):
    i += 1
  else:
    ans += b // c[i]
    b = b % c[i]
    i = 0
print(ans)