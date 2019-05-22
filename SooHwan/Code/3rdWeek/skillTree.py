def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        index = 0
        for sk in tree:
            if sk in skill:
                if skill[index] != sk:
                    break
                else:
                    index+=1
            if sk == tree[-1]:
                answer+=1
            

    return answer