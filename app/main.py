import utils

keys, values = utils.get_population()
print(keys, values)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Venezuela',
        'Population': 200
    }
]


country = input('Cual pais?: ')
result = utils.population_by_country(data, country)
print(result)