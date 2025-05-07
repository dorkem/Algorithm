def solution(x, n):
    answer = [x]
    num = x
    for i in range(n-1):
        num += x
        answer.append(num)
    return answer