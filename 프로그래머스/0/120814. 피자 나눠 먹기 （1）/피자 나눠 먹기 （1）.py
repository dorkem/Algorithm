def solution(n):
    cnt = 0
    while n>7:
        n = n - 7
        cnt += 1
    if n == 0:
        return cnt
    else:
        return cnt+1