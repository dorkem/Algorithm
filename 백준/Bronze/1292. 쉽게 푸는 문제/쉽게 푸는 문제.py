a = 1001
lst = [0]
for i in range(1,100):
  for j in range(i):
    lst.append(i)

s, m = map(int, input().split())
sum = 0
for i in range(s,m+1):
  sum += lst[i]
print(sum)