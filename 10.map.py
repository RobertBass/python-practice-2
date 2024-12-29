numbers = [1, 2, 3, 4]
transformNumbers = []
for number in numbers:
    transformNumbers.append(number * 2)

print(numbers)
print(transformNumbers)

transformFunct = lambda number: number * 5

transformNumbersMap = list(map(transformFunct, numbers))
print(transformNumbersMap)

numbers2 = [5, 6, 7, 8]
sum = lambda x, y: x + y
transformNumbersMap2 = list(map(sum, numbers, transformNumbersMap))
print(transformNumbersMap2)