from collections import Counter

def solution(s):
    cnt = Counter(s)
    return ''.join(sorted([c for c in cnt if cnt[c] == 1]))