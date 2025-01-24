def solution(n, arr1, arr2):
  answer, map_list = [], []
  arr = [arr1, arr2]

  for a in arr:
    map = []

    for a1 in a:
      x, y = [], a1
      
      while y >= 1:
        x.append(y%2)
        y //= 2
      
      if len(x) != n:
        for i in range(n-len(x)) : x.append(0)
      
      map.append(x[::-1])

    map_list.append(map)

  # 두 지도 결합
  for i in range(n):
    x = ''
    
    for j in range(n):
      
      if map_list[0][i][j] + map_list[1][i][j] == 0:
        x += ' '
      else: x += '#'
    
    answer.append(x)

  return answer