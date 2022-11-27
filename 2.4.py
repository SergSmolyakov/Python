import  math
num = int(input("Введите число: "))

if num > 9 and num < 99:
    num0 = math.floor(num / 10)
    num1 = math.floor(num % 10)
    if num0 < num1:
        print("yes")
    else: print("no")
elif num > 99 and num < 999:
    num0 = math.floor((num / 100)%10)
    num1 = math.floor((num / 10)%10)
    num2 = math.floor(num % 10)
    if num0 < num1 and num1 < num2:
        print("yes")
    else: print("no")
elif num > 999 and num < 9999:
    num0 = math.floor((num / 1000) % 10)
    num1 = math.floor((num / 100) % 10)
    num2 = math.floor((num / 10) % 10)
    num3 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3:
        print("yes")
    else: print("no")

elif num > 9999 and num < 99999:
    num0 = math.floor((num / 10000) % 10)
    num1 = math.floor((num / 1000) % 10)
    num2 = math.floor((num / 100) % 10)
    num3 = math.floor((num / 10) % 10)
    num4 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3 and num3 < num4:
        print("yes")
    else: print("no")
elif num > 99999 and num < 999999:
    num0 = math.floor((num / 100000) % 10)
    num1 = math.floor((num / 10000) % 10)
    num2 = math.floor((num / 1000) % 10)
    num3 = math.floor((num / 100) % 10)
    num4 = math.floor((num / 10) % 10)
    num5 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5:
        print("yes")
    else: print("no")
elif num > 999999 and num < 9999999:
    num0 = math.floor((num / 1000000) % 10)
    num1 = math.floor((num / 100000) % 10)
    num2 = math.floor((num / 10000) % 10)
    num3 = math.floor((num / 1000) % 10)
    num4 = math.floor((num / 100) % 10)
    num5 = math.floor((num / 10) % 10)
    num6 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5 and num5 < num6:
        print("yes")
    else: print("no")
elif num > 9999999 and num < 99999999:
    num0 = math.floor((num / 10000000) % 10)
    num1 = math.floor((num / 1000000) % 10)
    num2 = math.floor((num / 100000) % 10)
    num3 = math.floor((num / 10000) % 10)
    num4 = math.floor((num / 1000) % 10)
    num5 = math.floor((num / 100) % 10)
    num6 = math.floor((num / 10) % 10)
    num7 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5 and num5 < num6 and num6 < num7:
        print("yes")
    else: print("no")
elif num > 99999999 and num < 999999999:
    num0 = math.floor((num / 100000000) % 10)
    num1 = math.floor((num / 10000000) % 10)
    num2 = math.floor((num / 1000000) % 10)
    num3 = math.floor((num / 100000) % 10)
    num4 = math.floor((num / 10000) % 10)
    num5 = math.floor((num / 1000) % 10)
    num6 = math.floor((num / 100) % 10)
    num7 = math.floor((num / 10) % 10)
    num8 = math.floor(num % 10)
    if num0 < num1 and num1 < num2 and num2 < num3 and num3 < num4 and num4 < num5 and num5 < num6 and num6 < num7 and num7 < num8:
       print("yes")
    else: print("no")








