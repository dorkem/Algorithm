def solution(s):
    lst = list(s)
    lst.sort()
    arr = []
    for i in lst:
        if lst.count(i) == 1:
           arr.append(i)
    return "".join(arr)