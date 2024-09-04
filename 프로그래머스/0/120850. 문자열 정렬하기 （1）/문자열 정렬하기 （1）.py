def solution(my_string):
    answer = list(my_string)
    lst = []
    for i in answer:
        if ord(i) <= 65:
            lst.append(int(i))
    lst.sort()
    return lst