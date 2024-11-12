tc = int(input())
for i in range(1,tc+1):
   n = int(input())
   s = list(map(int, input().split()))
   p = sum(s)//n
   ans = 0
   for j in range(n):
      if s[j] <= p:
         ans+=1
   print(f"#{i} {ans}")