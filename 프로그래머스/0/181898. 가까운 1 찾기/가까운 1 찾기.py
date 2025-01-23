def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1 : return i
    else: return -1