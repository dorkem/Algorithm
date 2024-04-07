from collections import deque

q = deque(range(1, int(input())+1))

while len(q) > 1:
    q.popleft()
    q.rotate(-1)
print(q[0])