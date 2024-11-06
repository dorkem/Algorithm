tc = int(input())
for i in range(1,tc+1):
    n = int(input())
    arr = [[0 for _ in range(n+1)] for _ in range(n)]
    arr[0][1] = 1
    print(f"#{i}")
    for j in range(1,n):
        for k in range(1,n+1):
            arr[j][k] = arr[j-1][k-1] + arr[j-1][k]
    for j in range(n):
        word = ''
        for k in arr[j]:
            if k != 0:
                word += str(k)
        print(" ".join(word))