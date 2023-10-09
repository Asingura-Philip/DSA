# write a line of code that prompts the user to replace the middle number in the list with an
# integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

replace = int(input("enter number to replace middle number: "))
hat_list = [1, 2, 3, 4, 5]
hat_list[2] = replace
hat_list.pop()
print("length of list:", len(hat_list))
