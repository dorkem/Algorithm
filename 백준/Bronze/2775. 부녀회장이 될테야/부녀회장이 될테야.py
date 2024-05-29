a = int(input().strip())

for _ in range(a):
    floor = int(input())
    num = int(input())
    zero = [i for i in range(1,num+1)]
    for i in range(floor):
        for j in range(1, num):
            zero[j]+=zero[j-1]
    print(zero[-1])