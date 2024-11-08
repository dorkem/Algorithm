t = int(input())
for tc in range(1, t+1):
    n = list(map(int, input().split()))
    a = n[0] * n[4]
    if n[4] <= n[2]:
        charge = n[1]
    else:
        charge = n[1] + (n[4]-n[2])*n[3]
    b = charge

    if a < b:
        print(f"#{tc} {a}")
    else:
        print(f"#{tc} {b}")