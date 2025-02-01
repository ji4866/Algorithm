def solution(n):
    n_2 = bin(n)[2:]
    one_count = n_2.count('1')
    
    while True:
        n += 1
        n_2 = bin(n)[2:]

        if n_2.count('1') == one_count:
            break
            
    return n