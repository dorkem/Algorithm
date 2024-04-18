import sys
input = sys.stdin.readline
list = []
sum = 0
for _ in range(5):
  a = int(input())
  list.append(a)
  sum += a
list.sort()
print(sum//5)
print(list[2])
