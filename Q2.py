my_array = []

num_elements = int(input("How many elements do you want to add to the array? "))

for i in range(num_elements):

    element = input(f"Enter element {i+1}: ")

    my_array.append(element)

print("The final array is:", my_array)