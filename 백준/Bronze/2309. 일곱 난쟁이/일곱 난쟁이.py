a=[]
for i in range(9):
  high = int(input())
  a.append(high)

a.sort()
cnt = 0
for i in range(8):
  for j in range(i+1,9):
    if sum(a)-a[i]-a[j] == 100:
      del a[j]
      del a[i]
      cnt += 1
      break
  if cnt==1:
    break
for i in range(7):
  print(a[i])