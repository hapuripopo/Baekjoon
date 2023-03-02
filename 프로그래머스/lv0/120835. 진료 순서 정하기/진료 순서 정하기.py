def solution(emergency):
    sort_e = sorted(emergency, reverse=True)
    return [sort_e.index(x)+1 for x in emergency]