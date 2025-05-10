def solution(n):
    answer = str(bin(n))[2:]
    countNumberOne = answer.count('1')
    for i in range(n+1,1000001):
        iNum = str(bin(i)).count('1')
        if iNum == countNumberOne:
            answer = i
            break
    return answer