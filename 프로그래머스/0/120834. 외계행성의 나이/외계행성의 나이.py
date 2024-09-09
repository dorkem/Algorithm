def solution(age):
    answer = list(str(age))
    a = []
    for i in range(len(answer)):
        o = ord(answer[i])+49
        a.append(chr(o))
    return "".join(a)