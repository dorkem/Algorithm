a = int(input())
b = list(map(int, input().split()))
b.sort()
if a == 1:
    print(b[0]*b[0])
else:
    print(b[-1]*b[0])