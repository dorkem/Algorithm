N = int(input())
arr = list(map(int, input().split()))
T, P = map(int,input().split())
cnt = 0
for i in range(len(arr)):
    cnt += arr[i] // T
    if arr[i] % T != 0:
        cnt += 1
print(cnt)
print(f"{N//P} {N%P}")