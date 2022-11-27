import math
salary = int(input("Введите целое число: "))
banknote1 = 1
banknote3 = 3
banknote10 = 10
banknote25 = 25

countMoney = salary / banknote25
countBanknote25 = math.floor(countMoney)
countMoney = math.floor((countMoney - countBanknote25) * 25)
countOtherBanknote = countMoney / banknote10
countBanknote10 = math.floor(countOtherBanknote)
countOtherBanknote = math.floor((countOtherBanknote - countBanknote10) * 10 )
countOtherBanknote = countOtherBanknote / banknote3
countBanknote3 = math.floor(countOtherBanknote)
countOtherBanknote = math.floor((countOtherBanknote - countBanknote3) * 3 )
countOtherBanknote = countOtherBanknote / banknote1
countBanknote1 = math.ceil(countOtherBanknote)
countOtherBanknote = math.floor((countOtherBanknote - countBanknote1) * 1 )

print(f'Количество купюр 25: {countBanknote25}, Количество купюр 10: {countBanknote10}, Количество купюр 3: {countBanknote3},Количество купюр 1: {countBanknote1}')