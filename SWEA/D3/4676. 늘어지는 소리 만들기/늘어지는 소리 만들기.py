t = int(input())
for tc in range(1,t+1):
    arr = list(input())
    h = int(input())
    m = list(map(int,input().split()))
    m.sort()
    n = 0
    for i in range(h):
        arr.insert(m[i]+n, "-")
        n+=1
    print(f"#{tc} {''.join(arr)}")