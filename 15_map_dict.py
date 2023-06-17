items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'jeans',
        'price': 120
    },
    {
        'product': 'sudadera',
        'price': 70
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

#Colocar nuevo atributo:

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

# map() iterar y transformar de acuerdo a una función.
# map(funcion, lista a iterar)
# map() modifica array original, crea uno nuevo.
new_items = list(map(add_taxes, items))
print(new_items)
print(items)