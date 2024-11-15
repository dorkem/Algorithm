t = int(input())
for tc in range(1,t+1):
    m, d = map(int, input().split())
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = [4, 5, 6, 0, 1, 2, 3]
    index = (sum(month[:m])+d) % 7
    print(f"#{tc} {day[index-1]}")