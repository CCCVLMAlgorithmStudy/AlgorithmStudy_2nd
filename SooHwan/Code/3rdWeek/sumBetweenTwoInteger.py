def solution(a, b):
    answer = 0
    larger = a if a>b else b
    smaller = a + b - larger
    
    for num in range(smaller,larger+1):
        answer+=num
    return answer