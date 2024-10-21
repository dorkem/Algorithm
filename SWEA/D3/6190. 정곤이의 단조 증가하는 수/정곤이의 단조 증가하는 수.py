def increaseNum(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            return 0
    return 1

T = int(input())
for tc in range(T):
    value = -1
    N = int(input())
    A = list(map(int,input().split()))
    for i in range(N):
        for j in range(i+1,N):
            num = A[i] * A[j]
            if increaseNum(num) == 1:
                value = max(value, num)
    print(f"#{tc+1} {value}")