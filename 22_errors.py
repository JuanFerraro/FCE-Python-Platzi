
try: 
    print(0/0)
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad') # El programa se detiene.
    assert 1 != 1, 'Error: uno dif a uno?'
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

try:
    assert 1 != 1, 'Error: uno dif a uno?'
except AssertionError as error:
    print(error)


try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad') # El programa se detiene.
except Exception as error:
    print(error)

print('Hola')