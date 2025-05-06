def solution(n):
    answer = list(str(n))
    ans = [int(a) for a in answer]
    return ans[::-1]