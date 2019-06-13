def solution(nums):
    a = len(nums)//2
    b = len(set(nums))
    answer = a if a<b else b
    return answer