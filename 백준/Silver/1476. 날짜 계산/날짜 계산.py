a, b, c = map(int,input().split())
E = 1
S = 1
M = 1
i = 1
while True:
    if a == E and b == S and c == M:
        print(i)
        break
    E = (E%15)+1
    S = (S % 28) + 1
    M = (M % 19) + 1
    i+=1