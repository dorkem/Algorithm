num = int(input())
a=[0]*(num+1)

for i in range(1,num+1):
    for j in range(i, num+1, i):
        a[j] += i
print(sum(a[1:num+1]))