t = 10
for tc in range(1,t+1):
    tn = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    mv = 0
    
    for i in range(100):
        row = sum(arr[i])
        ans = 0
        for j in range(100):
            ans += arr[j][i]
        mv = max(mv, row, ans)
    ans = 0
    for i in range(100):
        ans += arr[i][i]
    mv = max(mv, ans)

    ans = 0
    for i in range(100):
        ans += arr[i][99-i]
    mv = max(mv, ans)

    print(f"#{tc} {mv}")