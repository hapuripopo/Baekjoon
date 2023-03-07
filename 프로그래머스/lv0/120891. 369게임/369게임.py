def solution(order):
    return len([x for x in str(order) if x in '369'])