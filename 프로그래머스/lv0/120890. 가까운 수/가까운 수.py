def solution(array, n):
    answer = sorted([x-n for x in sorted(array)], key= lambda x: abs(x))
    return answer[0]+n