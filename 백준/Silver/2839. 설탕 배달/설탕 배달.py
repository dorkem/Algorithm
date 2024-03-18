a = int(input())
if a%5==0:
  print(a//5)
else:
  count=0;
  while a>0:
    a-=3
    count+=1
    if a%5==0:
      print(count+a//5)
      break
    elif a==1 or a==2:
      print(-1)
      break
    elif a==0:
      print(count)
      break