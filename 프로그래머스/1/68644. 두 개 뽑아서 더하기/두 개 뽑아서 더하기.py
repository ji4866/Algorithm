def solution(numbers):
    list_ = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if i+1 > len(numbers)-1:break
            if numbers[i]+numbers[j] in list_:continue
            x = numbers[i]+numbers[j]
            list_.append(x)

    return sorted(list_)