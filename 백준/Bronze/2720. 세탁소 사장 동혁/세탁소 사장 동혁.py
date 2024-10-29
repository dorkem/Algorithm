tc = int(input())
for i in range(tc):
    money = int(input())
    arr = []
    
    for coin in [25, 10, 5, 1]:
        cnt = money // coin
        arr.append(cnt)
        money %= coin

    print(" ".join(map(str, arr)))
