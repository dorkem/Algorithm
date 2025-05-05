t = int(input())
for i in range(t):
    a = input()
    b = list(map(int, input().split()))
    b.sort()
    ans = b[-1] - b[0]
    print(f"#{i+1} {ans}")