set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union de conjuntos:
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)  # Con operador |

# Interseccion:
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b) # Con operador &

# Diferencia:
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) # Con operador -

# Diferencia Simetrica:
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b) # Con operador ^