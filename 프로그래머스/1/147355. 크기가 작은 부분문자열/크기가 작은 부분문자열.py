def solution(t, p):
    index, count = 0,0
    while True:
        b = t[index:index+len(p)]
        if len(b) < len(p):break
        if int(b) <= int(p):count+=1
        index += 1
    return count