def print_params(a = 2, b = 'строка', c = True):
    print(a, b, c)


print_params(4, 'число')
print_params( 12,None, False)
print_params(26)
print_params()


print_params(b=25)
print('Функция print_params(b=25) работает')
print_params(c = [1,2,3])
print('Функция print_params(c = [1,2,3]) работает')

values_list = [125, True, 'Анастасия']

values_dict = {'a':1312.2024, 'b':"Ручка", 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)
print('Функция print_params(*values_list_2, 42) работает')