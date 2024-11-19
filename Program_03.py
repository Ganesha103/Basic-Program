# Program to find the string with all vowels remove
string = input("Enter the string:")
vowels = ""  # create String
for j in string: # for each number in the original list,
    if j == "a" or j == "e" or j == "i" or j =="o" or j == "u" or j == "A" or j == "E" or j == "I" or j == "O" or j =="U": # Find Vowels in string
        pass
    else:
        vowels = vowels + j # add character in vowels
print("The New string:",vowels)