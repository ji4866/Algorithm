def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        list_ = []
        
        for j in range(len(arr1[i])):
            list_.append(arr1[i][j] + arr2[i][j])
        
        answer.append(list_)    
    return answer