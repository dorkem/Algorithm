def solution(num, k):
    answer = list(str(num))
    if str(k) in answer:
        return answer.index(str(k)) + 1
    else:
        return -1
    