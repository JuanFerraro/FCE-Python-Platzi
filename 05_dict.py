# Forma clasica
""" dict = {}
for i in range (1,5):
    dict[i] = i * 2

print(dict)

dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2) """

# Generar dic a partir de una lista
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

# Otro ejemplo
names = ['juan', 'sebastian', 'barrios', 'ferraro']
ages = [12, 13, 14]

persons = {names[i]:ages[i] for i in range(len(names)-1)}
print(persons)