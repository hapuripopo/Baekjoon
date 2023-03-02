def solution(age):
    return ''.join([chr(97+int(x)) for x in str(age)])