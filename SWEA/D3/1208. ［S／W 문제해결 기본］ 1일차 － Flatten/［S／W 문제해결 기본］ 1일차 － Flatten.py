for i in range(1, 11):
    dump = int(input())
    n = list(map(int, input().split()))
    for j in range(dump):
        n.sort()
        n[0]+=1
        n[-1]-=1
    print(f"#{i} {max(n)-min(n)}")