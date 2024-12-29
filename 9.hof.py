def increment(x):
    return x * 2

def hof(x, y, func):
    return x + func(y)

res =  hof(2, 4, increment)
print(res)