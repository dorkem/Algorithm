def solution(slice, n):
    cnt = 1
    while 1:
        if slice * cnt > n:
            return cnt
        elif n % slice == 0:
            return n//slice
        cnt += 1