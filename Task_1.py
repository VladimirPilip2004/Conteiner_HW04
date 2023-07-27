# Считает сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Введите число N: '))
list = []
count = 0
for i in range(1, n + 1):
    list.append(i)
    if i % 2 == 0:
        count = count + i
print(f"Список состоит из: {list}")
print(f"Сумма чётных чисел от 1 до {n} равна: {count}")