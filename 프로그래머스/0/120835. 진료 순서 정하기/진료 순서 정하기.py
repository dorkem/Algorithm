def solution(emergency):
    answer = sorted(emergency, reverse=True)
    result = []
    for value in emergency: 
        result.append(answer.index(value) + 1)
    return result