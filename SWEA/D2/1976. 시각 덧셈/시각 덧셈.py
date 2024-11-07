T = int(input())
for tc in range(1, T+1):
    arr = list(map(int,input().split()))

    min = arr[1] + arr[3]
    p = 0
    if min >= 60:
        min = min % 60
        p = 1

    time = arr[0] + arr[2] + p
    if time % 12 == 0:
        time = 12
    else:
        time = time % 12
       
    print(f"#{tc} {time} {min}")