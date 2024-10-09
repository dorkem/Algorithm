T = int(input())
for i in range(T):
    N, L = map(int,input().split())
    arr = [[0,0]]
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    dp = [[0]*(L+1) for _ in range(N+1)]

    for j in range(1, N+1):
        for k in range(1, L+1):
            score = arr[j][0]
            cal = arr[j][1]

            if k < cal:
                dp[j][k] = dp[j-1][k]
            else:
                dp[j][k] = max(dp[j-1][k], dp[j-1][k-cal]+score)
    
    print(f"#{i+1} {dp[N][L]}")
