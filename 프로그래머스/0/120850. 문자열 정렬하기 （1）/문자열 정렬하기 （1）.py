def solution(my_string):
    answer = []
    
    for s in my_string:
        try:
            answer.append(int(s))
        except:
            continue
            
    return sorted(answer)