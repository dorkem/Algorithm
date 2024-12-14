def solution(array):
    cnt = 0
    for i in range(len(array)):
        array[i] = str(array[i])
        words = array[i]
        cnt += words.count('7')
    return cnt