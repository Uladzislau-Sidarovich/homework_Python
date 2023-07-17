def recursion(a, b):
    if b == 0:
        return 1
    else:
        return a * recursion(a, b - 1)

a = int(input("введите число : "))
b = int(input("введите степень : "))
print(recursion(a, b))
