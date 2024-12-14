def solution(s):
    arr = set()
    while s != 1:
        for i in range(2, s+1):
            if s % i == 0:
                s //= i
                arr.add(i)
                break
    return sorted(list(arr))