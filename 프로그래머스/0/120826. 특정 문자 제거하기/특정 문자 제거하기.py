def solution(my_string, letter):
    answer = list(my_string)
    i = 0
    while i < len(answer):
        if answer[i] == letter:
            answer.pop(i)
        else:
            i+=1
    return "".join(answer)