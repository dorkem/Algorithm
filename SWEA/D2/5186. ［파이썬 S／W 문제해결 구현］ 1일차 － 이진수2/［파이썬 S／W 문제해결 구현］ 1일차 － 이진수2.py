t = int(input())
for i in range(t):
    n = input()
    a = list(n.split('.'))
    frac = float('0.' + a[1])
    answer = f'#{i+1} '
    count = 0

    while frac > 0:
        if count >= 13:
            answer = f'#{i+1} overflow'
            break
        frac *= 2
        bit = int(frac)
        answer += str(bit)
        frac -= bit
        count += 1

    print(answer)