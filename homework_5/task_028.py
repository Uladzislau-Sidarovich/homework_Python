def recsum(a,b):
    if b == 0:
        return a
    else:
        return 1 + recsum(a, b - 1)

a = int(input("введите число : "))
b = int(input("введите число : "))
print(recsum(a, b))