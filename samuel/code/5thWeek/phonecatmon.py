def solution(nums):
    return len(list(set(nums))) if len(list(set(nums))) < len(nums)//2 else len(nums)//2