import functools

numeros = [1,2,3,4]

#En funcion:
def acumulador (counter, item):
    return counter + item


result = functools.reduce(lambda counter, item: counter + item, numeros)
print(result)
result = functools.reduce(acumulador, numeros)
print('v2: ',result)

