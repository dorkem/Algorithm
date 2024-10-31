def bfs(r):
  global cnt
  visited[r] = cnt
  for i in lst[r]:
    if visited[i] == 0:
      cnt += 1
      bfs(i)


import sys

sys.setrecursionlimit(150000)

n, m, r = map(int, sys.stdin.readline().split())
lst = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  lst[a].append(b)
  lst[b].append(a)

for i in range(1, n):
  lst[i].sort()

cnt = 1
visited = [0] * (n + 1)
bfs(r)

for i in range(1, n + 1):
  print(visited[i])