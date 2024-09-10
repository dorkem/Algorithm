def solution(my_string):
    answer = list(my_string)
    for i in range(len(answer)):
        if answer[i].isupper():
            answer[i] = answer[i].lower() 
    answer.sort()
    return "".join(answer)
