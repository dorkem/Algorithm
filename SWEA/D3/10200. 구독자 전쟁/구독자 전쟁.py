t = int(input())
for tc in range(1,t+1):
    n, a, b = map(int,input().split())
    m = 0
    if n < a + b:
        m = a+b-n
    print(f"#{tc} {min(a,b)} {m}")