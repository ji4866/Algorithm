def solution(s):
    zeros, cnt = 0,0
    
    while s != '1':
        count = len(s) - s.count('0')
        x = bin(count)[2:]
        
        zeros += s.count('0')
        cnt += 1
    
        s = x
    
    return [cnt, zeros]