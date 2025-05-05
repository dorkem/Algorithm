t = int(input())
for i in range(t):
    a, b = input().split()
    b = list(b)
    answer = ""
    for j in b:
        answer += format(int(j,16), '04b')
    print(f"#{i+1} {answer}")