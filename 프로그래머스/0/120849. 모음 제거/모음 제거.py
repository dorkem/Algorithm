def solution(my_string):
    answer = list(my_string)
    a = []
    mo = ['a','e','i','o','u']

    for i in range(len(my_string)):
        if answer[i] in mo:
            continue
        else:
            a.append(answer[i])
    return "".join(a)