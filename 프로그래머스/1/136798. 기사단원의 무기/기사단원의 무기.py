def solution(number, limit, power):
    sum_ = 0

    for num in range(1, number+1):
        count = 0

        for i in range(1, int(num**(1/2))+1):
            if num % i == 0 :
                count += 1
                if i != num//i : count += 1
            if count > limit:
                count = power
                break
    
        sum_ += count
    
    return sum_