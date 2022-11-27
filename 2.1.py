xNum = int(input("Введите целое число x: "))
yNum = int(input("Введите целое число y: "))
res = 0

for i in range(xNum, yNum):
    if i % 2==0 or i % 3==0:
        res +=1
print(res)