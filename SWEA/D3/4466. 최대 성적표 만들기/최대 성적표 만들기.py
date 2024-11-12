t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    score = list(map(int, input().split()))
    score.sort(reverse=True)
    print(f"#{tc} {sum(score[0:m])}")