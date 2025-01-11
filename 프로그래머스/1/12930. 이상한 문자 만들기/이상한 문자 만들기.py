def solution(s):
    st_list = s.lower().split(' ')
    answer = ''
    
    for st in st_list:
        i, a = 0, []

        for s in st:
            if s == '':break
            if i%2 == 0:a.append(s.upper())
            else:a.append(s)
            i+=1

        x = ''.join(a)
        answer += x+' '
        
    return answer[:-1]