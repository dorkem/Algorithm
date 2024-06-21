def solution(my_string):
    answer = 0
    num = [str(i) for i in range(1,10)]
    for i in my_string:
        if i in num:
            answer += int(i)
    return answer