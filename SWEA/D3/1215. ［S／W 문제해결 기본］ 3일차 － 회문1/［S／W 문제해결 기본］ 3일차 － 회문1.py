for t in range(10):
    length = int(input())
    n = 8
    cnt = 0
    arr = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n-length+1):
            if arr[i][j:j+length] == arr[i][j:j+length][::-1]:
                cnt+=1
        
    for i in range(n):
        for j in range(n-length+1):
            
            char = ''
            for k in range(j,j+length):
                char += arr[k][i]
            if char == char[::-1]:
                cnt+=1
    
    print(f'#{t+1} {cnt}')