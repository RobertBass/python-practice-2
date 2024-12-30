def getPopulation():
    keys = ['ecu', 'col', 'arg']
    values = [300, 400, 500]
    return keys, values


def population_by_country(data, country):
    return list(filter(lambda item: item['country'] == country, data))
    