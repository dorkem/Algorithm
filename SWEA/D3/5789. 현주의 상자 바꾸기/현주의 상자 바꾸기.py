t = int(input())
for tc in range(1,t+1):
    n, q = map(int, input().split())
    arr = [0]*n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        for j in range(r-l+1):
            arr[j+l-1] = i
    print(f"#{tc} {' '.join(map(str, arr))}")