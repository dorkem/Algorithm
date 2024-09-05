def solution(n):
    cnt = 1
    s = 6
    while True:
        if (s*cnt) % n == 0:
            return cnt
        cnt += 1
        