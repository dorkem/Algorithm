t = int(input())
for tc in range(1,t+1):
    score = list(map(int, input().split()))
    sum = 0
    for i in range(len(score)):
        if score[i] < 40:
            sum += 40
        else:
            sum+=score[i]
    print(f"#{tc} {sum//len(score)}")