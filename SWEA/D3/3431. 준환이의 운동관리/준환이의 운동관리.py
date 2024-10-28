T = int(input())
for tc in range(1, T+1):
    l,u,x = map(int, input().split())
    result = 0
    if x < l:
        result = l-x
    elif l <= x <= u:
        result = 0
    else:
        result = -1
    print(f"#{tc} {result}")