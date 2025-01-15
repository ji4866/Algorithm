def solution(s, n):
    x = ''

    for i in s:
        c = ord(i)+n
        if i == ' ':
            x += ' '
        elif ord(i) >= ord('a') and c > ord('z'):
            c_n = c - ord('z') - 1
            c = ord('a')+c_n
            x += chr(c)
        elif ord(i) <= ord('Z') and c > ord('Z'):
            c_n = c - ord('Z') - 1
            c = ord('A')+c_n
            x += chr(c)
        else : x += chr(c)
    return x