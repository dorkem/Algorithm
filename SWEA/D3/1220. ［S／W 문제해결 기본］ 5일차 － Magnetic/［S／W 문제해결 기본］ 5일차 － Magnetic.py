T = 10
for tc in range(T):
    n = int(input())
    cnt = 0
    arr =[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        flag = 0
        for j in range(n):
            if arr[j][i] == 1:
                flag = 1
            elif arr[j][i] == 2 and flag == 1:
                cnt+=1
                flag = 0
    print(f"#{tc+1} {cnt}")