from collections import deque

def dfs(visited, graph, v):
    visited[v] = 1
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] != 1:
            dfs(visited, graph, i)


def bfs(visited, graph, v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        a = queue.popleft()
        print(a, end = ' ')
        for i in graph[a]:
            if visited[i] != 1:
                queue.append(i)
                visited[i] = 1 

n, m, v = map(int, input().split())
graph = [[]*(n+1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)
dfs(visited1, graph, v)
print()
bfs(visited2, graph, v)