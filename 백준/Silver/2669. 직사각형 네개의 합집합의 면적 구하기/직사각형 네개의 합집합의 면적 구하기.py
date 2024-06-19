a = []
x = 0
y = 0
for i in range(4):
    a.append(list(map(int,input().split())))
    x = max(x, a[i][0], a[i][2])
    y = max(y, a[i][1], a[i][3]) 

m = [[0]*x for _ in range(y)]

for i in range(4):
    for j in range(a[i][1],a[i][3]):
        m[j][a[i][0]:a[i][2]] = [1] * (a[i][2] - a[i][0])

print(sum(sum(row) for row in m))