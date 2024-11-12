testcase = int(input())
for tc in range(1,testcase+1):
   a, b = map(int,input().split())
   sq = [1,4,9,121,484]
   cnt = 0
   for i in sq:
      if i >= a and i <= b:
         cnt += 1
   print(f"#{tc} {cnt}")