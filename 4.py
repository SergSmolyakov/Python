import math
x1 = float(input("Введите координату x точки А "))
y1 = float(input("Введите координату y точки А "))
x2 = float(input("Введите координату x точки B "))
y2 = float(input("Введите координату y точки B "))
result = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'A ({x1},{y1}); B({x2},{y2}) -> {result}')