def solution(s):
    try:
        int(s)
    except:
        return False

    else:
        if len(s) == 4 or len(s) == 6 : return True
        else : return False