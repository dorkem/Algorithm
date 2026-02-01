arr = [None] * 101
seen = int(input())
count = 0

for i in range(seen):
    move = list(map(int, input().split()))
    if arr[move[0]] == None:
        arr[move[0]] = move[1]
    elif arr[move[0]] != None and arr[move[0]] != move[1]:
        count += 1
        arr[move[0]] = move[1]

print(count)