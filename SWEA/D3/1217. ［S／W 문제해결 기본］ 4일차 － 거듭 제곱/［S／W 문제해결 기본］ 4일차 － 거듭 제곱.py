T = 10
for i in range(1,T+1):
    a = int(input())
    N, M = map(int, input().split())
    print(f"#{i} {N ** M}")