t = int(input())
for i in range(t):
    N = int(input())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    dirx = 0
    x,y = 0,0

    for j in range(1, N**2+1):
        lst[x][y] = j
        
        nx = x+ dir[dirx][0]
        ny = y+ dir[dirx][1]
        
        
        if nx < 0 or nx>=N or ny < 0 or ny>=N or lst[nx][ny]!=0:
            dirx = (dirx+1)%4
            nx = x+ dir[dirx][0]
            ny = y+ dir[dirx][1]

        x, y = nx, ny
    print(f"#{i+1}")    
    for a in lst:
        print(" ".join(map(str, a)))