t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    twin = n-m
    uni = m-twin
    print(f"#{tc} {uni} {twin}");