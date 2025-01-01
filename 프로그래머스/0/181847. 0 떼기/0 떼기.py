def solution(n_str):

    for n in n_str:
        if n != '0':
            index = n_str.index(n)
            break
            
    n_str[:index].replace('0','')
    
    return n_str[:index].replace('0','') + n_str[index:]