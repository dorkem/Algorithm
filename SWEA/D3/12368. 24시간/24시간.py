tc = int(input())
for i in range(1,tc+1):
   t, nt = map(int, input().split())
   print(f"#{i} {(t + nt) % 24}")