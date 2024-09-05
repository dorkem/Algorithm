def solution(n):
    i = 1000
    a = 0
    cnt = 0
    while 1:
        cnt = a*a
        if cnt > n:
            return 2
        if n == cnt:
            return 1
        a+=1
        