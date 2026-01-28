result = ''
str = input()
for i in str:
    if i.upper() == i : result += i.lower()
    else : result += i.upper()
print(result)