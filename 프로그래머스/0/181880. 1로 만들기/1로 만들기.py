def solution(num_list):
    result = 0
    
    for i in num_list:
        j = i
        while j != 1:
            if j%2 == 0: 
                j //= 2
            else :
                j = (j-1)//2

            result += 1
    return result