T = int(input())
for tc in range(T):
    N = int(input())
    cnt = 1
    arr = [0]*5001
    for i in range(N):
        A, B = map(int,input().split())
        for j in range(A, B + 1):
            arr[j] += 1
    P = int(input())
    print(f"#{tc+1}",end =" ")
    for i in range(P):
        c = int(input())
        print(arr[c], end=" ")
    print()