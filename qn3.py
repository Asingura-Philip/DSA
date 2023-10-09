"""
Your task is to write a program which removes all the number repetitions from the list.
 The goal is to have a list in which all the numbers appear not more than once.
"""


input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]

unique_list = []

# Iterate through the input list and add unique numbers to the unique_list
for number in input_list:
    if number not in unique_list:
        unique_list.append(number)

# Print the list with repetitions removed
print("List with repetitions removed:", unique_list)
