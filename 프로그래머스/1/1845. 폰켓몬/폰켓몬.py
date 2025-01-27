def solution(nums):
    n = len(nums)//2 # 가질 수 있는 폰켓몬 갯수
    return min(n, len(set(nums)))