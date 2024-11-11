a, b = map(int, input().split())
n = set(list(map(int, input().split())))
m = set(list(map(int, input().split())))
print(len(n-m)+len(m-n))