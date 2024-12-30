import mod

keys, values = mod.getPopulation()
print(keys, values)

data = [{'country': key, 'population': value} for (key, value) in zip(keys, values)]
print(data)

country = input("Que pais quieres verificar? ")
res = mod.population_by_country(data, country)
print(res)