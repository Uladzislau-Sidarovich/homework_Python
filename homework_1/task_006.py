s = input('Введите 6-значный номер билета: ')
if len(s) != 6:
    print(f'Число {s} не 6-ти значное')
else:
    res1 = 0
    res2 = 0
    for i in range(len(s)//2):
        res1 += int(s[i])
        res2 += int(s[len(s)//2 + i])
    if res1 == res2:
        print(f'{s} счастливый номер')
    else:
        print(f'{s} не счастливый номер')