import random;

countries = ['ecu', 'col', 'chi', 'arg', 'bra']
population = { country: random.randint(1, 100) for country in countries}
print(population)

result = { country: population for (country, population) in population.items() if population > 50 }
print(result)

text = "Hola soy Roberto"
unique = { l: l.upper() for l in text if l in 'aeiou' }
print(unique)