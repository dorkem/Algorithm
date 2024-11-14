t = int(input())
for tc in range(1,t+1):
    arr = set(list(input()))
    if len(arr) == 2:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")