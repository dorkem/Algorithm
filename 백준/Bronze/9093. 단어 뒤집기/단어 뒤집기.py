import sys
a = int(input())
for _ in range(a):
    str = sys.stdin.readline()
    words = list(str.split())
    lst = []
    for a in words:
        lst.append(a[::-1])
    print(" ".join(lst))