n = int(input('В-те 1-ю сторону: '))
m = int(input('В-те 2-ю сторону: '))
k = int(input('В-те кол-во долек: '))
if k < n*m and (k % n == 0 or k % m == 0):
    print('Yes')
else:
    print('No')