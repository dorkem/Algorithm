import sys
a = int(sys.stdin.readline())
for i in range(a):
  H,W,N = map(int, input().split())
  f = N % H
  num = N // H + 1
  if f == 0:
    f = H
    num -= 1
  
  print(f*100+num)
  