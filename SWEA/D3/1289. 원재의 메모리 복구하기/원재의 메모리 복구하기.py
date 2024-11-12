testcase = int(input())

for tc in range(1, testcase + 1):
    target = input().strip()
    count = 0
    if target[0] == '1':
        count += 1
    for i in range(1, len(target)):
        if target[i] != target[i - 1]:
            count += 1
    print(f"#{tc} {count}")