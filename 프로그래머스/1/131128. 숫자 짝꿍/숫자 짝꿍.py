def solution(X,Y):
    answer, str_ = '', ''

    x, y = set(X), set(Y)
    xy = x & y # 공통으로 들어가는 숫자
        
    #print('xy : ', xy)

    if len(xy) == 0:
        return '-1'
    elif xy == {'0'}:
        return '0'

    unique = list(xy)

    for i in unique:
        count_x, count_y = X.count(i), Y.count(i)
        count_ = min(count_x, count_y)
        str_ += i*count_
        #print(str_)

    answer = sorted(str_, reverse = True)

    return ''.join(answer)