t = 10
for tc in range(1,t+1):
    l = int(input())
    arr = list(map(int,input().split()))
    n = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] ==  "I":
            for j in range(int(order[i+2])):
                arr.insert(int(order[i+1])+j, int(order[i+3+j]))
        elif order[i] == "D":
            for j in range(int(order[i+2])):
                arr.pop(int(order[i+1]))
    print(f"#{tc} {' '.join((map(str,arr[:10])))}")