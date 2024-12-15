def solution(number, k):
    cnt = 1
    answer = 0

    while k != cnt:
        answer+=2
        cnt+=1
        if answer >= len(number):
            answer %= len(number)
    return number[answer]