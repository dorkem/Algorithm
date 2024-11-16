t = int(input())  # 테스트 케이스 수 입력

for tc in range(1, t + 1):
    arr = list(input())
    char_count = {}
    for char in arr:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    lst = []
    for char, count in char_count.items():
        if count % 2 == 1:
            lst.append(char)
    if lst:
        lst.sort() 
        print(f"#{tc} {''.join(lst)}")
    else:
        print(f"#{tc} Good")
