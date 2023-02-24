from collections import Counter

def solution(array):
    mode = Counter(array).most_common()
    
    if len(mode) > 1:
        if mode[0][1] == mode[1][1]:
            return -1
    
    return mode[0][0]