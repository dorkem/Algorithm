def solution(keyinput, board):
    x = board[0]//2
    y = board[1]//2
    location = [0, 0]

    for i in keyinput:
        if i == "left" and location[0]-1 >= -x:
            location[0] -= 1
        elif i == "right" and location[0]+1 <= x:
            location[0] += 1
        elif i == "up" and location[1]+1 <= y:
            location[1] += 1
        elif i == "down" and location[1]-1 >= -y:
            location[1] -= 1 
    return location