def solution(order):
    answer = list(str(order))
    cnt = 0
    for i in range(len(answer)):
        if answer[i] in "369":
            cnt+=1
    return cnt