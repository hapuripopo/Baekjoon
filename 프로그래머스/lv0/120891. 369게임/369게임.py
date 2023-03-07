def solution(order):
    clap = ['3', '6', '9']
    return len([x for x in str(order) if x in clap])