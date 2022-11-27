a = int(input("Введите количество чисел, которое собираетесь вводить: "))
max_num1 = 0
max_num2 = 0

for i in range(a):
    b = int(input(f"Введите '{i + 1}-е' целое число: "))
    if b > max_num1:
        max_num2 = max_num1
        max_num1 = b
    elif b > max_num2:
        max_num2 = b
print(f"Первое максимальное число найдено: {max_num1}")
print(f"Второе максимальное число найдено: {max_num2}")
