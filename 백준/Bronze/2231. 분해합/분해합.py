a = int(input().strip())

def mini(a):
    for num in range(max(1,a-63), a):
        b = num + sum(map(int,str(num)))
        if b == a:
            return num
    return 0
    
c = mini(a)
print(c)