a = float(input("Введите число a: "))  # Ввод числа a
n = 1
s = 0

while s <= a:
    s += 1 / n
    n += 1

# Вывод всех значений n, при которых сумма больше a
for i in range(1, n):
    print(i)