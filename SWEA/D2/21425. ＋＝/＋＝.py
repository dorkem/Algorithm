tc = int(input())
for i in range(tc):
    x,y,n = map(int,input().split())
    count = 0
    while n>=x and n>=y:
        if x < y:
            x += y
        else:
            y += x
        count += 1
    print(count)