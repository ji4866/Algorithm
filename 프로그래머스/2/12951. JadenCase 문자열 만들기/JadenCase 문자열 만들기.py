def solution(s):
    st = s.split(' ')
    list_ = [
        i[:1].upper()+i[1:].lower() for i in st
    ]
    
    return ' '.join(list_)
