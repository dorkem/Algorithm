for _ in range(int(input())):
    A, B = map(str, input().split())
    c = int(A,2)+int(B,2)
    print(bin(c)[2:])
