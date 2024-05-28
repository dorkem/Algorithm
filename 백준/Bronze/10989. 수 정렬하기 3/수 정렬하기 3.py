import sys
input = sys.stdin.readline

a = int(input())
b = [0] * 10001
for _ in range(a):
    b[int(input())] += 1

for i in range(len(b)):
    if b[i] != 0:
        for _ in range(b[i]):
            print(i)