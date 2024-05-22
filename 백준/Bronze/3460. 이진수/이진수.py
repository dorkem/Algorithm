a = int(input())
for _ in range(a):
    num = int(input())
    b = [int(i) for i in bin(num)[2:]]
    b.reverse()

    for i in range(len(b)):
        if b[i]==1:
            print(i, end=" ")