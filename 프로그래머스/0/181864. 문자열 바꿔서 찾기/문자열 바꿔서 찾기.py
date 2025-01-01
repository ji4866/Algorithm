def solution(myString, pat):
    answer = ''

    for st in myString:
        if st == 'A': answer += 'B'
        else: answer += 'A'
            
    if pat in answer: return 1
    else: return 0