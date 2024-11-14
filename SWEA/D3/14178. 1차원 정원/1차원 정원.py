t = int(input())
for tc in range(1,t+1):
    n, d = map(int,input().split())
    i = 0
    cnt = 0
    while n > i:
        i += d * 2 + 1
        cnt += 1
    print(f"#{tc} {cnt}")