# Program to Number of unique character
string = input("Enter the string:")
count = 0
unique_list = []  # a list for Unique Character
for i in string: # for each number in the original list
    if i not in unique_list: # Checking character in string or not
        unique_list.append(i) # If character in string append then
count = len(unique_list)      # Find the length
print("Number of unique character are:",count)
