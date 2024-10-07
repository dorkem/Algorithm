T = int(input())
for t in range(T):
    N = int(input())
    M = N//2
    answer = 0
    arr = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        if i<=M:
            for j in range(M-i, M+i+1):
                answer += arr[i][j]
        else:
            for j in range(i-M, N-(i-M)):
                answer += arr[i][j]
    
    print(f'#{t+1} {answer}')