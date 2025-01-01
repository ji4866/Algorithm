def solution(myString):
    answer = ''
    st = [s if s >= 'l' else 'l' for s in myString ]
    for s in st:answer += s
    return answer