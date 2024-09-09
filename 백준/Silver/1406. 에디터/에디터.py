import sys

l = list(input())
r = []
n = int(input())

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == "L" and l:
        r.append(l.pop())
    elif a[0] == "D" and r:
        l.append(r.pop())
    elif a[0] == "B" and l:
        l.pop()
    elif a[0] == "P":
        l.append(a[1])

print("".join(l + list(reversed(r))))