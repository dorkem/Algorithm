t = 10
for tc in range(1,t+1):
    first = int(input())
    second = list(map(int, input().split()))
    third = int(input())
    fourth = list(input().split())
    for i in range(len(fourth)):
        order = ""
        if fourth[i] == 'I':
            for j in range(int(fourth[i+2])):
                second.insert(int(fourth[i+1])+j, int(fourth[i+3+j]))

        elif fourth[i] == 'D':
            for j in range(int(fourth[i+2])):
                second.pop(int(fourth[i+1]))
        elif fourth[i] == 'A':
            for j in range(int(fourth[i+1])):
                second.append(int(fourth[i+2+j]))
    print(f"#{tc} {' '.join(map(str, second[:10]))}")