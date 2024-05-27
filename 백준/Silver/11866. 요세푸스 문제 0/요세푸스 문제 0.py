a, b = map(int,input().split())
lst = [i for i in range(1,a+1)]
hi = []
start = 0

while len(lst) != 0:
    start = (start+b-1) % len(lst)
    hi.append(lst.pop(start))

print("<" + ", ".join(map(str, hi)) + ">")