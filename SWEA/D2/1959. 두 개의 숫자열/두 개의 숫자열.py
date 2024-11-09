t = int(input())
for tc in range(1, t+1):
    a, b = map(int,input().split())
    arr1 = list(map(int, input().split())) #5
    arr2 = list(map(int, input().split())) #3

    if a > b:
        n = arr1
        arr1 = arr2
        arr2 = n

    max = 0
    for i in range(len(arr2)-len(arr1)+1):
        sum = 0
        for j in range(min(a,b)):
            sum += arr1[j] * arr2[j+i]
        if max <= sum:
            max = sum
    
                
    print(f"#{tc} {max}")