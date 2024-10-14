T = 10
for tc in range(1,T+1):
    N = int(input().strip())
    arr = list(map(int,input().split()))
    c = 0
    for i in range(2, N-2):
        lst = []
        if arr[i] >= arr[i-1] and arr[i]>=arr[i-2] and arr[i]>=arr[i+1] and arr[i]>=arr[i+2]:
            mv = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
            c += arr[i] - mv
    print(f"#{tc} {c}")