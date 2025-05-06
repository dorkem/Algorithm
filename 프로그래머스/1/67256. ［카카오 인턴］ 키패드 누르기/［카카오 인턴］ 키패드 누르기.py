def solution(numbers, hand):
    answer = ""
    keypad = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    left = keypad['*']
    right = keypad['#']
    for i in numbers:
        if i in (1, 4, 7):
            left = keypad[i]
            answer += 'L'
        elif i in (3, 6, 9):
            right = keypad[i]
            answer += 'R'
        else:
            leftD = abs(left[0]-keypad[i][0]) + abs(left[1] - keypad[i][1])
            rightD = abs(right[0]-keypad[i][0]) + abs(right[1] - keypad[i][1])
            
            if leftD < rightD:
                left = keypad[i]
                answer += 'L'
            elif rightD < leftD:
                right = keypad[i]
                answer += 'R'
            else:
                if hand == "right":
                    right = keypad[i]
                    answer += 'R'
                else :
                    left = keypad[i]
                    answer += 'L'
    return answer