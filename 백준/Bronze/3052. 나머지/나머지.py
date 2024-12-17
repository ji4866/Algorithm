list_ = []

for i in range(10):
  n = int(input())
  x = n%42
  list_.append(x)
  
print(len(set(list_)))