tc = int(input())
for i in range(tc):
    n = int(input())
    arr = list(map(str, input().split()))
    for j in range(n//2):
        if len(arr) % 2 == 0:
            a = arr.pop(n//2 + j)
            arr.insert(j * 2 + 1, a)
        else:
            a = arr.pop(n//2 + j + 1)
            arr.insert(j * 2 + 1, a)
    print(f"#{i + 1}", ' '.join(arr))