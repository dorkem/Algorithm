import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(r):
    global cnt
    visited[r] = cnt
    for i in graph[r]:
        if visited[i] == 0:
            cnt+=1
            dfs(i)
               

n, m, r = map(int,input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for i in range(m):
    u, v = map(int,input().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1, n + 1):
    graph[i] = sorted(graph[i], reverse=True)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])