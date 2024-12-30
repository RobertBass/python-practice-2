import sys
import re
import time
import collections

print(sys.path)

text = 'Mi numero de telefono es 311 123 121, el codigo de pais es el 57, mi numero de suerte es el 7'
result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
localTime = time.localtime()
result = time.asctime(localTime)
print(timestamp)
print(localTime)
print(result)

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)