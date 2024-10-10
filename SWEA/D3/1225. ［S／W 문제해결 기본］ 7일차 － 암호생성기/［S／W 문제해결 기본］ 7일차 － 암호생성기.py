T = 10
for tc in range(1,T+1):
    a = int(input())
    arr = list(map(int, input().split()))
    while arr[-1] != 0:
        for i in range(1,6):
            if arr[-1] == 0:
                break
            if arr[0] >= i:
                arr[0] -= i
            else:
                arr[0] = 0
            arr.append(arr.pop(0))
    print(f"#{tc} {' '.join(map(str, arr))}")