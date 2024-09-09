a, b = map(int, input().split())
l = [i for i in range(1, a+1)]
r = []
index = 0

while len(r) != a:
    index = (index + b - 1) % len(l)
    r.append(l.pop(index))

print(f"<{', '.join(map(str, r))}>")