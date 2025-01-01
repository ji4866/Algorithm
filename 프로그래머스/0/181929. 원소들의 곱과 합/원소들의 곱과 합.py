def solution(num_list):
    m = 1
    for num in num_list:
        m *= num
    if m < sum(num_list)**2:
        return 1
    else:
        return 0