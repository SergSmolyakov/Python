# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом
import re

numDecimal = input("Введите дробное число: ")

def isfloat(a):
    find = re.findall(r"\d*\.\d+", a)
    if find:
        return True
    else:
        return False

print(isfloat(numDecimal))