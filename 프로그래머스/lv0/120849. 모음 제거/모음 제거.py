def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    return ''.join([s for s in my_string if s not in vowel])