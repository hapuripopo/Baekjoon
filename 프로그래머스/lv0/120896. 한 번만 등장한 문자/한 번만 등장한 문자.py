from collections import Counter

def solution(s):
    return ''.join(sorted([c for c in s if Counter(s)[c] == 1]))