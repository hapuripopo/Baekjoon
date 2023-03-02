def solution(rsp):
    answer = ''
    for x in rsp:
        if x == '2':
            answer += '0'
        elif x == '5':
            answer += '2'
        else:
            answer += '5'
    return answer