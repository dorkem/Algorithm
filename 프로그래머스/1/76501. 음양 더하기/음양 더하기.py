def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]
        sum += absolutes[i]
    return sum