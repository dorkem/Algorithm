k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

left = 1
right = max(arr)
result = 0

while left <= right:
    mid = (left+right)//2
    count = 0
    for i in arr:
        count += i//mid
    if count >= n:
        result = mid
        left = mid+1
    
    else:
        right = mid-1

print(result)