import functools

numbers = [1, 2, 3, 4, 5]
res = functools.reduce(lambda acum, x: acum + x, numbers)
print(res)

def sum(acum, x):
    print(acum)
    #print(x)
    return acum + x

res2 = functools.reduce(sum, numbers)
print(res2)