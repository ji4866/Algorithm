def solution(s):
    a, b = [], []
    
    for i in s:
        if i == '(' : a.append(i)
        else : b.append(i)

        if len(b) > len(a) : return False
    
    if len(b) != len(a) : return False
    else: return True