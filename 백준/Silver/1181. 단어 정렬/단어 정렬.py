arr = []
for _ in range(int(input())):
    arr.append(input().strip())
arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x:(len(x),x))
for e in arr:
    print(e)
 