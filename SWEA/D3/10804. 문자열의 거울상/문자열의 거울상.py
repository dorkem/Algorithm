t = int(input())
for tc in range(1,t+1):
    n = input()
    n = n[::-1]
    s = ""
    for i in n:
        if i == 'b':
            s += 'd'
        elif i == 'd':
            s += 'b'
        elif i == 'p':
            s += 'q'
        else:
            s += 'p'
    print(f"#{tc} {s}")