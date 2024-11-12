t = 10
for tc in range(1,t+1):
    n, pw = map(int,input().split())
    pw = list(str(pw))
    stack = []
    for i in pw:
        if not stack:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print(f"#{tc} {int(''.join(stack))}")