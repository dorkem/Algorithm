def solution(n):
    answer = list(map(int, n.split(" ")))
    answer.sort()
    st = f"{answer[0]} {answer[-1]}"
    return st