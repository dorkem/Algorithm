t = int(input())
for i in range(t):
    a = input()
    cards = input()
    cardList = [int(a) for a in cards]
    
    answer = [0]*10
    for card in cardList:
        answer[card] += 1

    maxCount = max(answer)
    maxNumber = -1

    for j in range(9,-1,-1):
        if answer[j] == maxCount:
            maxNumber = j
            break    

    print(f"#{i+1} {maxNumber} {maxCount}")    