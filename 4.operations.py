aCountries = {'ecu', 'col', 'chi', 'arg', 'bra'}
bCountries = {'ecu', 'par', 'per', 'uru', 'ven', 'bol'}

countries = aCountries.union(bCountries)
print(countries)
print(len(countries))
print(aCountries | bCountries)

countries = aCountries.intersection(bCountries)
print(countries)
print(len(countries))
print(aCountries & bCountries)

countries = aCountries.difference(bCountries)
print(countries)
print(len(countries))
print(aCountries - bCountries)

countries = aCountries.symmetric_difference(bCountries)
print(countries)
print(len(countries))
print(aCountries ^ bCountries)

countries = aCountries.issubset(bCountries)
print(countries)

countries = aCountries.issuperset(bCountries)
print(countries)