# 3.12 Вводим с клаиватуры строку. Необходимо развернуть подстроку между первой и последней буквой "о". Если она только одна или её нет - то сообщить, что буква "о" -одна или не встречается
str = "торнадо"
ch = "о"
str1 = (str.find(ch))
str2 = (str.rfind(ch)-1)
# for i in range(len(str)1, 2, -1):
# print(str1, str2)
revStr = str[::-1]
print(revStr[str1:str2])