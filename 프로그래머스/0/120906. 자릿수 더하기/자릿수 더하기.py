def solution(n):
    answer = list(str(n))
    answer = sum(int(num) for num in answer)
    
    return answer