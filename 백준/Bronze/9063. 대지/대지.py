tc = int(input())
xarr = []
yarr = []
for i in range(tc):
   x, y = map(int,input().split())
   xarr.append(x)
   yarr.append(y)

xmin = min(xarr)
xmax = max(xarr)
ymin = min(yarr)
ymax = max(yarr)

print((xmax-xmin)*(ymax-ymin))