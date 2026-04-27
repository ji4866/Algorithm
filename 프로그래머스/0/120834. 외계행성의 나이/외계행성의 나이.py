def solution(age):
    result = ''
    age = str(age)
    age_cd = ['a','b','c','d','e','f','g','h','i','j']
    
    for i in age:
        result += age_cd[int(i)]
    return result