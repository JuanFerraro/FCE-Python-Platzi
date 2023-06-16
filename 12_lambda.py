def increment(x):
    return x + 1

result = increment(10)
print(result)

increment_v2 = lambda x : x + 1
result = increment_v2(20)
print(result)

full_name = lambda name, last_name: f'Nombre completo: {name.title()} {last_name.title()}'
nombre = full_name('Juan', 'Barrios')
print(nombre)