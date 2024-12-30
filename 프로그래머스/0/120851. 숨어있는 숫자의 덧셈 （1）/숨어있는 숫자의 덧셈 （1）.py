def solution(my_string):
    answer = 0
    num = list(map(str, list(range(10))))
    
    for s in my_string:
        if s in num:
            answer += int(s)
            
    return answer