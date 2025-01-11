def solution(arr):
    a = arr.copy()
    
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i] : a[i] = ''
        
    b = [i for i in a if i != '']
    return b