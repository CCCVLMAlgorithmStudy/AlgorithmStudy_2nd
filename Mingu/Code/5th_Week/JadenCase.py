# def capitalize(i):
#     return i.capitalize()
def solution(s):
    return " ".join(list(map(lambda x:x.capitalize(),s.split(" "))))