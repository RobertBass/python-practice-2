numbers = []
for element in range(1,11):
     numbers.append(element)
    
print(numbers)

numbers = [element for element in range(11, 21)]
print(numbers)

numbers = [element for element in range(1, 21) if element % 2 == 0]
print(numbers)