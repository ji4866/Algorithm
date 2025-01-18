def solution(n):
    x, y, sum_ = n//3, n%3, 0
    a = [y]
    
    while x > 0:
        y = x%3
        x //= 3
        a.append(y)
    
    c = len(a)-1
    
    for i in a:
        sum_ += i * 3**c
        c -= 1
        
    return sum_