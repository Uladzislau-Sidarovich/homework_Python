N = int(input('Введите количество элементов списка : '))
A_entered = input("Введите через пробел элементы списка: ").split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = (X - A_num[0])
    index = 0
    for i in range(1, N):
        count = (X - A_num[i])
        if count < min:
            min = count
            index = i
    print(
        f'Число {A_num[index]} в списке наиболее близко по величине к числу {X}, их разница составляет {(X - A_num[index])}')
