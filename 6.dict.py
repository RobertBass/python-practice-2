import random

dict = {}
for i in range(1,6):
    dict[i] = i * 2
print(dict)

dict = { i: i * 2 for i in range(1,6)}
print(dict)

countries = ['ecu', 'col', 'chi', 'arg', 'bra']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

popularion = { country: random.randint(1, 100) for country in countries}
print(popularion)

names = ['Roberto', 'Bruno', 'Emilio', 'Nicolas', 'Emma']
ages = [38, 13, 8, 6, 2]
print(list(zip(names, ages)))
family = {name: age for (name, age) in zip(names, ages)}
print(family)