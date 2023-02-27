import math
def solution(n):
    i = 1
    while(True):
        if (n * i) % 6 == 0:
            i = n * i / 6
            break;
        i += 1
        
    return i