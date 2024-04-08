def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
           [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    score = [0] * 3

    for i in range(len(answers)):
        if pattern[0][i%len(pattern[0])] == answers[i]:
            score[0] += 1
        if pattern[1][i%len(pattern[1])] == answers[i]:
            score[1] += 1
        if pattern[2][i%len(pattern[2])] == answers[i]:
            score[2] += 1
    
    high = max(score)
    a = []
    for i in range(len(score)):
        if score[i] == high:
            a.append(i+1)
    return a