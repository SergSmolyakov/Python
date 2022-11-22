dayNum = int(input("Введите номер дня "))
if dayNum > 0 and dayNum < 6:
    print(f'{dayNum} -> нет')
elif dayNum == 6 or dayNum == 7:
    print(f'{dayNum} -> да')
else:print("Введено число вне диапазона 1-7")
