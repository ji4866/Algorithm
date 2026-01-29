ary = list(map(int, input().split()))
a = [1, 1, 2, 2, 2, 8]
for i in range(len(ary)):
    print(a[i] - ary[i], end = ' ')
    