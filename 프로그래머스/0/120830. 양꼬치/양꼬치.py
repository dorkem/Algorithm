def solution(n, k):
    if n>9:
        a = n//10
        a *= 2000
    else:
        a = 0
    answer = 12000*n+2000*k-a
    return answer