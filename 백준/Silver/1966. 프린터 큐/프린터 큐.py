a = int(input())

for _ in range(a):
    num, rem = map(int, input().split())
    imp = list(map(int, input().split()))
    n = imp[rem]
    cnt = 0
    while imp:
        if imp[0] < max(imp):
            imp.append(imp.pop(0))
        else:
            if rem == 0: break
            imp.pop(0)
            cnt += 1
        if rem > 0:
            rem= rem-1
        else:
            rem = len(imp)-1
    print(cnt+1)