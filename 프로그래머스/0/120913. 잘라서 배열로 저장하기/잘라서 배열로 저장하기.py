def solution(my_str, n):
    arr = []
    for i in range(0, len(my_str), n):
        arr.append(my_str[i:i+n])
    return arr