def bfs(r):
  global cnt
  queue = deque([r])
  visited[r] = cnt
  while queue:
    a = queue.popleft()
    for i in lst[a]:
      if visited[i] == 0:
        queue.append(i)
        cnt+=1
        visited[i] = cnt
      
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

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
