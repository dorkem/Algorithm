a = int(input())
num = 0
if a < 100:
    print(a)
else:
    num += 99
    for i in range(100, a + 1):
        n = list(str(i))
        if (int(n[1]) - int(n[0])) == (int(n[2]) - int(n[1])):
            num += 1

    print(num)