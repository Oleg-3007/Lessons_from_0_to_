#num = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
numbers = list(range(3, 21))
n = int(input("Введите код 1 :"))
key1 = list(range(1, n))
key2 = list(range(1, n))
pairs = []
result =  ""
for i in key1:
    for j in key2:
        a = i
        b = j
        if a >= b:
            continue
        else:
            condition = n % (a + b)
            if condition == 0:
                pairs.append ([a, b])
                result = result + str (a) + str (b)
print("Пары чисел :", *pairs)
print( "Код 2 :", result )

