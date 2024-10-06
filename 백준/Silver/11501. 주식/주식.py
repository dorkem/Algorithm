T = int(input())
for i in range(T):
    N = int(input())
    lst = list(map(int,input().split()))
    answer = 0
    max = 0

    for j in lst[::-1]:
        if j >= max:
            max = j
        else:
            answer += max - j
    print(answer)