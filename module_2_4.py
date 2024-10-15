numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
print ("Numbers =", numbers)
for i in range ( 2, len (numbers) + 1 ) :
    for j in range ( 2, i //2 + 1 ):
        if (i % j) == 0 :
            #print (i)
            not_primes. append (i)
            break
    else:
            primes. append (i)
            #print(i)

print ("Primes:", primes)
print ("Not Primes:", not_primes)#break
