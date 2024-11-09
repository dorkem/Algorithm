T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    distance = 0
    speed = 0

    for _ in range(N):
        command = list(map(int, input().split()))
        
        if command[0] == 1: 
            speed += command[1]
        elif command[0] == 2: 
            speed = max(speed - command[1], 0)

        distance += speed
    print(f"#{test_case} {distance}")
