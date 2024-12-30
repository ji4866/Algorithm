def num_(list_):
    sum_ = ''
    list_ = list(map(str,list_))
    for i in list_:
        sum_ += i
    return int(sum_)


def solution(num_list):
    odd, even = [], []

    for i in num_list:
        if i%2 == 1:
            odd.append(i)
        else:
            even.append(i)
    return num_(odd)+num_(even)