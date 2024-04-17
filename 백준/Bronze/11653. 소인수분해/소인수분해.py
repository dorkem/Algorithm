a = int(input())
while 1:
  if a == 1 :
    break
  for i in range(2, a+1):
    if a%i==0:
      print(i)
      a //= i
      break