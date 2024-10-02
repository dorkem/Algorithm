def dfs(graph, n, visited):
    global cnt
    cnt+=1
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(graph, i, visited)
    
c_num = int(input())
connect = int(input())
cnt = 0

graph = [[] for _ in range(c_num + 1)]
for i in range(connect):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,c_num):
    graph[i].sort()

visited = [0]*(c_num+1)
dfs(graph, 1, visited)
print(cnt-1)