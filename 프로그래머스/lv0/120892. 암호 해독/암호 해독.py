def solution(cipher, code):
    return ''.join([v for k, v in enumerate(cipher) if (k+1)%code==0])