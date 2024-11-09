t = int(input())
for tc in range(1, t+1):
    day = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    m1, d1, m2, d2 = map(int,input().split())
    d = day[m1]-d1+1
    if m1 == m2:
        print(f"#{tc} {d}")
        continue
    else:
        for i in range(m1+1,m2):
            d+=day[i]
        d += d2
    print(f"#{tc} {d}")