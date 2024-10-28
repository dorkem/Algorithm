play, win = map(int,input().split())

winRate = (win*100)//play
left, right = 0, 1000000000
result = -1

while left <= right:
    mid = (left+right)//2
    rate = ((win+mid)*100) // (play+mid)

    if rate > winRate:
        result = mid
        right = mid - 1
    else:
        left = mid + 1
print(result)