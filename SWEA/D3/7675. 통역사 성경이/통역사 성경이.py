def name(word):

    if not (word[0].isupper()):
        return False

    if(word[-1] in ['.', '!', '?']):
        word = word[:-1]

    for w in word[1:]:
        if not (w.islower()):
            return False

    return True


T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    full_sentence = ''
    end = 0
    signiture = ['.', '!', '?']
    
    # 전체 문장 받기
    while(end < N):
        sentence = input()
        full_sentence += sentence

        for s in signiture:
            end += sentence.count(s)
 
    num_to_name = []
    answer = 0
    
    for word in full_sentence.split():

        if(name(word)):
            answer += 1

        if(word[-1] in ['.', '!', '?']):

            num_to_name.append(answer)
            answer = 0
    
    print("#%d %s" %(test_case, ' '.join(map(str, num_to_name))))
