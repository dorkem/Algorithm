t = int(input())
for tc in range(1,t+1):
    n = int(input())
    sum = 0
    for i in range(n):
        p, x = map(float, input().split())
        sum += p*x
    print(f"#{tc} {sum:.6f}")