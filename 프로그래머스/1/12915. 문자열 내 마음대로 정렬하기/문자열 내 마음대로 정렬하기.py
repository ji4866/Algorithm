def solution(strings, n):
    answer, st_dict = [], {}
    
    st = list(set([string[n] for string in strings]))
    st.sort()
    
    for s in st:
        y = [string for string in strings if s == string[n]]
        st_dict[s] = y
    
    for v in st_dict.values():
        if len(v)>1 : v.sort()
    
    return sum(st_dict.values(), [])