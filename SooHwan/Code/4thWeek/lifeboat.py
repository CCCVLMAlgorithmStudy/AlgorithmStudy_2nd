def solution(people, limit):
    answer = 0
    people.sort()
    lastSavedSmallPeople = 0
    lastSavedBigPeople = len(people)-1
    
    while lastSavedSmallPeople<=lastSavedBigPeople:
        if(lastSavedBigPeople==lastSavedSmallPeople):
            lastSavedSmallPeople+=1
            answer+=1
        elif people[lastSavedBigPeople]+people[lastSavedSmallPeople]>limit:
            lastSavedBigPeople-=1
            answer+=1
        else:
            lastSavedBigPeople-=1
            lastSavedSmallPeople+=1
            answer+=1

    return answer