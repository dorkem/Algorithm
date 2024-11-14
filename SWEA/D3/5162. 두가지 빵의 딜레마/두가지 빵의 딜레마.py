t = int(input())
for tc in range(1,t+1):
    a, b, c = map(int, input().split())
    print(f"#{tc} {c//min(a, b)}")