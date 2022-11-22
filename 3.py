coordinateNum = int(input("Введите номер четверти (1-4) "))
if coordinateNum == 1:
    print("x < 0; y > 0")
elif coordinateNum == 2:
    print("x > 0; y > 0")
elif coordinateNum == 3:
    print("x < 0; y < 0")
elif coordinateNum == 4:
    print("x > 0; y < 0")
else: print("Введен не корректный номер четверти")