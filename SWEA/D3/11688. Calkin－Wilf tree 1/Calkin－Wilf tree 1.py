testcase = int(input())
for tc in range(1,testcase+1):
   n = 1
   m = 1 
   node = list(input())
   for i in range(len(node)):
      if node[i] == 'L':
         m = n+m
      else:
         n = n+m
   print(f"#{tc} {n} {m}")