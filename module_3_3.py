def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
print("=" * 15)

print_params()
print_params(26)
print_params(4, "MustanG")
print_params( 48,True, "Gorilla")
print("=" * 15)

print_params(b = 25)        # Работает
print_params(c = [1,2,3])   # Работает
print("=" * 15)

values_list = [3.14, "KarabiN", False]
values_dict = {'a':1976, 'b':"KarabiN", 'c':False}
print_params(*values_list)
print_params(**values_dict)
print("=" * 15)

values_list_2 = [ 1980,"Olimpic"]
print_params(*values_list_2, "Games")       # Pаботает