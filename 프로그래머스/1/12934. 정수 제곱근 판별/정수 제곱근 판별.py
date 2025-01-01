def solution(n):
    x = round(n**(1/2),5)
    if n == x**2:return int((x+1)**2)
    else: return -1