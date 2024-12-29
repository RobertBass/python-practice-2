items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 200
    },
    {
        'product': 'zapatos',
        'price': 300
    }
]
getPrices = lambda item: item['price']
prices = list(map(getPrices, items))
print(prices)

def setTaxes(item):
    item['taxes'] = item['price'] * .15
    return item

list(map(setTaxes, items))
print(items)