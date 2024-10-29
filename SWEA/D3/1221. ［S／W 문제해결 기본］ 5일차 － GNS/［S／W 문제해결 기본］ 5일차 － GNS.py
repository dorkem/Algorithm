tc = int(input())
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for i in range(1,tc+1):
    n = input().split()
    a = input().strip().split()
    arr = [num.index(j) for j in a]
    arr.sort()
    lst = [num[j] for j in arr]
    print(f"#{i}")
    print(f"{' '.join(map(str, lst))}")