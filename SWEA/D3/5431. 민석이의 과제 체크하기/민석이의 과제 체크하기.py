t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    print(f"#{tc}",end=" ")
    for i in range(1, n+1):
        if i in arr:
            continue
        else:
            print(i,end=" ")
    print()