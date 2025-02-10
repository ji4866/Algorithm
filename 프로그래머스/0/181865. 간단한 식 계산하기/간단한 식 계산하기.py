def solution(binomial):
    st = ['+', '-', '*']
    
    for s in st:
        if s in binomial:
            op = s
            idx = binomial.find(op)
            break
            
    if op == '+':
        return int(binomial[:idx-1]) + int(binomial[idx+2:])
    elif op == '-':
        return int(binomial[:idx-1]) - int(binomial[idx+2:])
    else:
        return int(binomial[:idx-1]) * int(binomial[idx+2:])