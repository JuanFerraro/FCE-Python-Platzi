#Create
set_countries = {'Col', 'Mex', 'Arg', 'Esp'}

size = len(set_countries)
print(size)

# Preguntar por un elemento
print('Col' in set_countries)
print('col' in set_countries)

# Add
set_countries.add('Pe')
set_countries.add('Pe')  # No agrega 2 veces lo mismo.
print(set_countries)

# Update
set_countries.update({'It', 'Ale', 'Ecu'})
print(set_countries)

# Remove
set_countries.remove('Ale')
set_countries.remove('It')
# Si intento eliminar uno que no esté lanza error.
# Si no sé si esta un elemento y quiero removerlo utilizo:
set_countries.discard('Por')
print(set_countries)

#Eliminar todo el conjunto
set_countries.clear()
print('Conjunto vacio: ', set_countries)
