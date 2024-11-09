t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = set()
    i = 1
    while len(arr) != 10:
        num = n * i
        word = list(str(num))
        arr.update(word)
        i += 1
    print(f"#{tc} {num}")