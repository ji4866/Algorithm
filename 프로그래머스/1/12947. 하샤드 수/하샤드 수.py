def solution(x):
    x_list = list(map(int, str(x)))
    return x % sum(x_list) == 0