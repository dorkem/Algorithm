tc = int(input())
for i in range(tc):
    num = int(input())
    left, right = 1, num
    result = 0
    while left <= right:
        mid = (left+right)//2
        jump = ((mid+1)*mid)//2

        if jump <= num:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    print(result)