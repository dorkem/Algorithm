T = int(input())
for tc in range(1, T+1):
    n = int(input())
    money = [50000,10000,5000,1000,500,100,50,10]
    arr = [0]*8
    for i in money:
        if n == 0:
            break
        if i > n:
            arr[money.index(i)] = 0
        else:
            k = n // i
            arr[money.index(i)] = k
            n -= k * i
    print(f"#{tc}")
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()