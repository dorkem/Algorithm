def solution(babbling):
    b = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for i in babbling:
        for j in b:
            i = i.replace(j,' ')
        if i.strip() == '':
            cnt+=1
    return cnt