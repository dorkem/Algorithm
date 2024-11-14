t = 10 
for tc in range(1,t+1):
    l = int(input())
    arr = list(map(int,input().split()))
    o = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] == "I":
            for j in range(int(order[i+2])):
                arr.insert(int(order[i+1])+j, order[i+j+3]) 
    print(f"#{tc} {' '.join(map(str, arr[:10]))}")