def solution(numlist, n):
    d_list = []
    
    for num in numlist:
        d = abs(n-num)
        if d in d_list:
            idx = d_list.index(d)
            if num > numlist[idx]: d_list[idx] += 0.5
            else : d += 0.5
        d_list.append(d)
        
    idx = [i for i in range(len(numlist))]
    result = [i for i in zip(d_list, idx)]
    
    result.sort()
    
    answer = [numlist[r[1]] for r in result]
    return answer