# CONJUNTOS

set_countries = {'ecu', 'col', 'mex', 'arg'}

# VALIDATIONES
print('col' in set_countries)
print('per' in set_countries)

# ADD
set_countries.add('per')
print(set_countries)
print('per' in set_countries)
set_countries.update({'bol', 'uru'})
print(set_countries)

# REMOVE
set_countries.remove('col')
print(set_countries)
#set_countries.remove('par')
set_countries.discard('par')
print(set_countries)
set_countries.clear()
print(set_countries)