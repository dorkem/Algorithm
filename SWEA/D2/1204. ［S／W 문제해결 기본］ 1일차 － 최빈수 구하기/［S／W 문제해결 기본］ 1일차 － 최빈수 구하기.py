a = int(input().strip())

for i in range(a):
    many = [0] * 101
    num = int(input().strip())
    scores = list(map(int, input().split()))  

    for score in scores:
        many[score] += 1

    max_count = max(many)
    mode_score = 0

    for score in range(101):
        if many[score] == max_count:
            mode_score = score

    print(f"#{i + 1} {mode_score}")