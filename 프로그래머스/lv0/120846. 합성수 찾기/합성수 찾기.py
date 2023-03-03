def solution(n):
    answer=[]
    for i in range(3, n+1):
        for j in range(2, i):
            if i % j == 0:
                answer.append(i)
                break
        
    return len(answer)