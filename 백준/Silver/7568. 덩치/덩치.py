a = int(input())
lst = []
rank = []
c = []

for _ in range(a):
  b = list(map(int, input().split()))
  lst.append(b)

ranks = [1] * a

for i in range(a):
  for j in range(a):
    if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
      ranks[i] += 1
  ranks[i] = str(ranks[i])
print(" ".join(ranks))