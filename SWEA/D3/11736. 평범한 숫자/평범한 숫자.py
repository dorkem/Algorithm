t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(arr)-1):
        left, right = arr[i-1], arr[i+1]
        if arr[i] != min(left, right, arr[i]) and arr[i] != max(arr[i], left, right):
            ans += 1
    print(f"#{tc} {ans}")