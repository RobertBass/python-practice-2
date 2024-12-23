aCountries = {'ecu', 'col', 'chi', 'arg', 'bra'}
bCountries = {'ecu', 'par', 'per', 'uru', 'ven', 'bol'}

# UNION OF SETS
countries = aCountries.union(bCountries)
print(countries)
print(len(countries))
print(aCountries | bCountries) # WITH OPERATOR

# INTERSECTION OF SETS
countries = aCountries.intersection(bCountries)
print(countries)
print(len(countries))
print(aCountries & bCountries) # WITH OPERATOR

# DIFFERENCE OF SETS
countries = aCountries.difference(bCountries)
print(countries)
print(len(countries))
print(aCountries - bCountries) # WITH OPERATOR

# SYMMETRIC DIFERENCE OF SETS (ONLY NOT REPEATED VALUES)
countries = aCountries.symmetric_difference(bCountries)
print(countries)
print(len(countries))
print(aCountries ^ bCountries) # WITH OPERATOR

countries = aCountries.issubset(bCountries)
print(countries)

countries = aCountries.issuperset(bCountries)
print(countries)