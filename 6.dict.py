import random

# NORMAL FUNCTION
dict = {}
for i in range(1,6):
    dict[i] = i * 2
print(dict)

# COMPREHENSION DICT
dict = { i: i * 2 for i in range(1,6)}
print(dict)

# NORMAL FUNCTION
countries = ['ecu', 'col', 'chi', 'arg', 'bra']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

# COMPREHENSION DICTS
popularion = { country: random.randint(1, 100) for country in countries}
print(popularion)

# JOINING LISTS
names = ['Roberto', 'Bruno', 'Emilio', 'Nicolas', 'Emma']
ages = [38, 13, 8, 6, 2]
print(list(zip(names, ages)))
family = {name: age for (name, age) in zip(names, ages)}
print(family)