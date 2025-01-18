def solution(s):
    english = {'zero':'0','one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    x, answer = '', ''
    for st in s:
        try:int(st)
        except:
            x += st
            if x in english.keys():
                answer += english[x]
                x = ''
        else:answer += st
    return int(answer)
        