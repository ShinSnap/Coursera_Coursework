largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" :
        break

    try: 
        num = int(num)
    except :
        print('Invalid input')
        continue

    if smallest == None and largest == None :
        smallest = num
        largest = num
    elif num < smallest :
        smallest = num
    elif num > largest :
        largest = num

print('Maximum is', largest)
print('Minimum is', smallest)