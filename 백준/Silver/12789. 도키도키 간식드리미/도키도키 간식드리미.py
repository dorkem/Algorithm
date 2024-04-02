a = int(input())
stack = []
line = list(map(int, input().split()))
i = 1

while line or stack:
    if line and line[0] == i:
        line.pop(0)
        i += 1
    elif stack and stack[-1] == i:
        stack.pop()
        i += 1
    elif line:
        stack.append(line.pop(0))
    else:
        print("Sad")
        break
else:
    print("Nice")
