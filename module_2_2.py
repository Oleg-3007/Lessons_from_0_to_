numbe1 = int(input ( ))
numbe2 = int(input ( ))
numbe3 = int(input ( ))
if numbe1 == numbe2 and numbe1 == numbe3:
    print (3)
elif numbe1 == numbe2 or numbe1 == numbe3 or numbe2 == numbe3:
    print (2)
elif numbe1 != numbe2 and numbe1 != numbe3:
    print (0)
