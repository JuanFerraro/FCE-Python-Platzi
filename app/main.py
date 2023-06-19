import utils

def run():
    keys, values = utils.get_population()
    print(keys, values)
    country = input('Cual pais?: ')
    result = utils.population_by_country(data, country)
    print(result)

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

if __name__ == '__main__':
    run()