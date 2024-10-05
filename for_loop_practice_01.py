numbers = [1232, 2131, 12312, 123124, 3543, 3456657, 565434, 2355645]

max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number

print("The maximum number in the list is " + str(max_number))
