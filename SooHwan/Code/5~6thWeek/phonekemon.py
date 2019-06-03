def solution(nums):
    answer = 0
    canGet = len(nums)//2
    kinds = len(set(nums))
    answer = kinds if kinds<canGet else canGet
    return answer