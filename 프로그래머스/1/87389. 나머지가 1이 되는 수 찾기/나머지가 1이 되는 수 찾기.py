def solution(n):
    answer = 2
    while 1:
        if n % answer == 1:
            return answer
        else:
            answer += 1