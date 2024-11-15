t = int(input())
for tc in range(1,t+1):
    arr = []
    maxLen = 0
    for i in range(5):
        st = list(input())
        arr.append(st)
        if len(st) > maxLen:
            maxLen = len(st)
    for i in range(5):
        if len(arr[i]) < maxLen:
            for j in range(maxLen - len(arr[i])):
                arr[i].append("")
    print(f"#{tc}",end=' ')
    for i in range(maxLen):
        for j in range(5):
            print(arr[j][i], end = '')
    print()