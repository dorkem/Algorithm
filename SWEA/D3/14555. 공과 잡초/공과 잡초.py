t = int(input())
for tc in range(1,t+1):
    arr = list(input())
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == '(':
            if arr[i+1] == ')' or arr[i+1] == '|':
                cnt += 1
        elif arr[i] == '|':
            if arr[i+1] == ')':
                cnt += 1
    print(f"#{tc} {cnt}")