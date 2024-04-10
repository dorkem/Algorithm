park = [0]*101
A,B,C = map(int,input().split())
sum = 0
for _ in range(3):
  start, end = map(int, input().split())
  for i in range(start, end):
    park[i] += 1

for i in park:
  if i == 1:
    sum+=A
  elif i == 2:
    sum+=B*2
  elif i == 3:
    sum+=C*3

print(sum)