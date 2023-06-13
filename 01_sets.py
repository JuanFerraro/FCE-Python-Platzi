# Conjuntos: Se pueden modificar, sin orden, sin duplicados

set_countries = {'Col', 'Mex', 'Arg', 'Esp'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 6}
print(set_numbers)
print(type(set_numbers))

set_types = {1, 'hola', False, 12.98}
print(set_types)

# Conjunto a partir de string
set_from_string = set('hola')
print(set_from_string)  # lo divide por caracteres

set_from_tuple = set(('abc', 'def', 'abc'))
print(set_from_tuple)

numbers = [1, 2, 3, 4, 1, 2, 3, 4, 1]
set_numbers = set(numbers)
print(set_numbers)  # No imprime repetidos
unique_numbers = list(set_numbers)
print(unique_numbers)