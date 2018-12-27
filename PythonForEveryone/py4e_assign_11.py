# Regex import
import re

samptxt = open('regex_sum_164712.txt')

numbers = int()

for line in samptxt:
    # Regex capture only the numbers per line
    newline = re.findall('[0-9]+',line)
    if len(newline) < 1 : continue
    
    # Add each value found in a line into total sum
    for value in newline :
        numbers = numbers + int(value)

print(numbers)
