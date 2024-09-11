def solution(array, n):
    answer = list(array)
    cnt = 0
    b = []
    for i in range(len(array)):
        answer[i] = abs(array[i]-n)
    a = min(answer)
    for i in range(len(answer)):
        if answer[i] == a:
            cnt+=1
            b.append(answer.index(answer[i]))
    return min(array, key=lambda x: (abs(x - n), x))