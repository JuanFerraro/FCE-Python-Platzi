import collections  # Utilidad para manejar listas
import time
import re
import sys
print(sys.path)

text = 'Mi numero de id es 00110110201, el código postal es 0033'
result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

numeros = [1, 2, 2, 3, 1, 1, 4, 5, 3, 6]
counter = collections.Counter(numeros)
print(counter)
