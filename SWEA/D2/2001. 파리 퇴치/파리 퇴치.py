total = int(input())
for i in range(total):
    index, space = map(int,input().split())
    arr = []
    for _ in range(index):
        row = list(map(int, input().split()))
        arr.append(row)
        
    lst = [[0 for _ in range(index+1)] for _ in range(index+1)]
    for j in range(1, index+1):
        for k in range(1,index+1):
            lst[j][k] = arr[j-1][k-1] + lst[j-1][k] + lst[j][k-1] - lst[j-1][k-1]
    
    large = 0
    for j in range(index-space+1):
        for k in range(index-space+1):
            sum = lst[j+space][k+space] - lst[j][k+space] - lst[j+space][k] + lst[j][k]

            if large < sum:
                large = sum
    print(f"#{i+1} {large}")
