def solution(mystring, indices):
    answer = ''
    for i in range(len(mystring)):
        if i not in indices : answer += mystring[i]
    return answer