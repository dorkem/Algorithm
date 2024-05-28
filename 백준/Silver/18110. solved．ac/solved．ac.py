import sys
input = sys.stdin.readline

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

a = int(input().strip())
if a:
    b = [int(input()) for _ in range(a)]
    b.sort()
    nn = roundUp(a * 0.15)
    print(roundUp(sum(b[nn:-nn] if nn else b) / (a - 2 * nn)))
else:
    print(0)