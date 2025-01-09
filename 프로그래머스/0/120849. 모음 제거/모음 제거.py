def solution(my_string):
    a = ['a','e','i','o','u']
    answer = list(my_string)
    
    for s in my_string:
        if s in a : answer.remove(s)
        
    return ''.join(answer)