x, y, w, h = map(int, input().split())
x = min(w-x, x)
y = min(h-y, y)
print(min(x,y))