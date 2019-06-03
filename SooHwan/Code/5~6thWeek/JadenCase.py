def solution(s):
    words = s.split(" ")
    for i,w in enumerate(words):
        words[i] = w.lower().capitalize()
    
    return " ".join(words)