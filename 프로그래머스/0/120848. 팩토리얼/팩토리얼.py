import math
def solution(n):
    a = [0]*11
    for i in range(1,11):
        a[i] = math.factorial(i)
        if a[i] == n:
            return i
    for i in range(10, 0, -1):
        if a[i] < n:
            return i
    return 0
            