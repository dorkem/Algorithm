def solution(cipher, code):
    a = []
    for i in range(code-1,len(cipher),code):
        a.append(cipher[i])
    return "".join(a)