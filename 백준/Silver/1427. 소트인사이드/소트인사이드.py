a = list(input())
b = sorted(list(map(int,a)),reverse=True)
print(''.join(str(i) for i in b))