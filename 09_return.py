def find_volume(length=1, width=1, depth=1): #Se puede asignar por defecto.
    return length * width * depth, width, 'Datos'
# Puedo devolver varios parametros como una tupla.


result = find_volume(2, 4, 6) # Si solo quiero enviar uno: (width=10)
result_v2, width, text = find_volume(width=10)
print(result)
print(result_v2)
print(width)
print(text)

