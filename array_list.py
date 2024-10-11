# Ensure the array (list) is defined before using it in the loop
elements = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'banana', 'apple']

# Create an empty hashmap (dictionary) to store the count of each element
element_count = {}

# Iterate over each element in the array using a for loop
for item in elements:
    if item in element_count:
        # If the item already exists in the dictionary, increment its count
        element_count[item] += 1
    else:
        # If the item doesn't exist in the dictionary, add it with a count of 1
        element_count[item] = 1

# Print the result
print("Element counts:", element_count)