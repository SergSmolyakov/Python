xCoord = int(input("Введите координату x не равную 0: "))
yCoord = int(input("Введите координату y не равную 0: "))

if xCoord == 0 or yCoord == 0:
    print("Одна или несколько координат равна 0")
else:
    if xCoord < 0 and yCoord > 0:
        print(f'x = {xCoord}; y = {yCoord} -> 1')
    elif xCoord > 0 and yCoord > 0:
        print(f'x = {xCoord}; y = {yCoord} -> 2')
    elif xCoord < 0 and yCoord < 0:
        print(f'x = {xCoord}; y = {yCoord} -> 3')
    elif xCoord > 0 and yCoord < 0:
        print(f'x = {xCoord}; y = {yCoord} -> 4')