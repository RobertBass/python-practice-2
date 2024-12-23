# NORMAL FUNCTION
numbers = []
for element in range(1,11):
     numbers.append(element)
print(numbers)

# COMPREHENSION LIST
numbers = [element for element in range(11, 21)]
print(numbers)

# COMPREHENSION LIST WITH CONDITIONS
numbers = [element for element in range(1, 21) if element % 2 == 0]
print(numbers)