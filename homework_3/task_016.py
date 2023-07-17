N = int(input("введите количество элементов : "))
A_entered = input("введите элементы списка через пробел : ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, которое необходимо найти в списке: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f'Число {X} встречается в списке {count} раз')