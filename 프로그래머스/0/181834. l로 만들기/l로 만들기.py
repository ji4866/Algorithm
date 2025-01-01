def solution(myString):
    answer = [s if s >= 'l' else 'l' for s in myString ]
    return ''.join(answer)