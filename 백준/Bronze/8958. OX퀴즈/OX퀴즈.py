import sys
a = int(sys.stdin.readline())

for _ in range(a):
  sum=0
  c=0
  b = list(sys.stdin.readline())
  for i in range(len(b)):
    if b[i] == "O":
      sum+=1+c
      c+=1
    else:
      c=0
  print(sum)