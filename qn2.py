"""
Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:
step 1: create an empty list named beatles;
step 2: use the append() method to add the following members of the band to the list: John Lennon, 
       Paul McCartney, and George Harrison;
step 3: use the for loop and the append() method to prompt the user to add the following members
       of the band to the list: Stu Sutcliffe, and Pete Best;
step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
step 5: use the insert() method to add Ringo Starr to the beginning of the list.
"""
# Step 1: Create an empty list named beatles
beatles = []

# Step 2:
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3:
band_members_to_add = ["Stu Sutcliffe", "Pete Best"]
for member in band_members_to_add:
    user_input = input(
        f"Do you want to add {member} to the Beatles band? (yes/no): ")
    if user_input.lower() == "yes":
        beatles.append(member)

# Step 4:
del beatles[3:5]

# Step 5:
beatles.insert(0, "Ringo Starr")

# Print the updated list
print("Updated Beatles band members:", beatles)
