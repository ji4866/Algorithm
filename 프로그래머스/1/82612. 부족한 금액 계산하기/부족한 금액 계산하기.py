def solution(price, money, count):
    for i in range(1, count+1):
        p = price * i
        money -= p
    
    if money >=0:return 0
    return abs(money)