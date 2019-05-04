def solution(a, b):
    dayName = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    dayCount = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(1,a):
        days += dayCount[i-1]
    days += b

    return dayName[(days+4)%7]