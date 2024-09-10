def solution(my_string):
    answer = list(my_string)
    a = []
    i = 0
    while i < len(my_string):
        if answer[i] not in a:
            a.append(answer[i])
        i += 1
    return "".join(a)
