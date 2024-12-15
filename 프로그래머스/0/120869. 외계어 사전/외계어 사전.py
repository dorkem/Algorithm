def solution(spell, dic):
    answer = 2

    for i in dic:
        leng = len(spell)
        for j in range(len(spell)):
            if spell[j] in i:
                leng -= 1
        if leng == 0:
            answer = 1
    
    return answer