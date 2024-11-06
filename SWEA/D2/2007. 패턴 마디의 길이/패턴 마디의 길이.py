tc = int(input())
for i in range(1,tc+1):
    word = input()
    j = 1
    cnt = 1
    while True:
        if word[:j] != word[j:j+j]:
            j += 1
        else:
            print(f"#{i} {j}")
            break