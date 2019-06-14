def solution(nums):
    half = len(nums)/2
    spieces = len(set(nums))
    if spieces < half:
         return spieces
    else:
        return half