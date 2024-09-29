immutable_var = 10, 20, 30, 3.14, 'generator', 1+8j
print (immutable_var)
#immutable_var [3] =  40  {кортеж не поддерживает изменение значений содержимого}
immutable_var = ([10, 20, 30, 3.14], ['generator'], 1+8j)
immutable_var [0] [3]= 40
immutable_var [1] [0]= 'pump'
print (immutable_var)