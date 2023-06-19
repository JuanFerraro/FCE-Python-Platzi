file = open('./23_text.txt')
# print(file.read()) #Lee todo
#print(file.readline()) #Lee linea a linea, más ligero
#print(file.readline()) #Lee linea a linea
#print(file.readline()) #Lee linea a linea

for line in file:
    print(line)

file.close() # Cerrar archivo, libera espacio.
#Python cierra automaticamente el archivo:
with open('./23_text.txt') as file:
    for line in file:
        print(line)