a1 = int(input('введите первый элемент ариф.прогрессии: '))
d = int(input('введите разность: '))
n = int(input('введите количество элементов ариф.прогрессии: '))
for i in range(n):
    print(a1 + i * d, end=' ')