from collections import deque

def bfs(n,k):
    queue = deque([(n, 0)])
    visited = set()
    visited.add((n, 0))
    mv = -1

    while queue:
        cur, cnt = queue.popleft()
        if cnt == k:
            mv = max(mv, int(cur))
            continue
        
        m = len(cur)
        for i in range(m):
            for j in range(i+1, m):
                if i==0 and cur[j] == '0':
                    continue
                num = list(cur)
                num[i], num[j] = num[j], num[i]
                num = ''.join(num)

                if (num,cnt+1) not in visited:
                    visited.add((num,cnt+1))
                    queue.append((num,cnt+1))
    return mv

n, k = input().split()
k = int(k)
result = bfs(n,k)
print(result if result!=-1 else -1)