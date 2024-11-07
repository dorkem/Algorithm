tc = int(input())
for i in range(1,tc+1):
    n, k = map(int, input().split())
    score = ["A+","A0","A-","B+","B0","B-","C+","C0","C-","D0"]
    arr = []
    for j in range(n):
        m, f, h = map(int, input().split())
        sc = m * 0.35 + f * 0.45 + h * 0.2
        arr.append(sc)
    my = arr[k-1]
    arr.sort(reverse = True)
    f = arr.index(my) 
    f //= (n//10)
    print(f"#{i} {score[f]}")