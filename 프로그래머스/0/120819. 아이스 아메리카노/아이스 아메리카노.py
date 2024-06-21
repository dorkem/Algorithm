def solution(money):
    answer = []
    a = money//5500
    answer.append(money//5500)
    answer.append(money-5500*a)
    return answer