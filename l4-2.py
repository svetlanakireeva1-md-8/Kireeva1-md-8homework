def d(n):
    return 100 / n
try:
    x = int(input("Введите число"))
except ValueError:
    print("Ошибка! Введите число, а не букву!")
try:
    print(d(x))
except ZeroDivisionError:
    print("Ошибка! Деление на ноль!")
