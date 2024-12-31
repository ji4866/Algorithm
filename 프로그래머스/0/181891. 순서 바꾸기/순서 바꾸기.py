def solution(num_list, n):
    list_1 = [num for num in num_list[n:]]
    list_2 = [num for num in num_list[:n]]
    return list_1+list_2