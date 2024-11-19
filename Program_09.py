# program number of word in string
string = input("Enter String")
count = 1     # count number of word
for i in range(len(string)):  # set in range and Running loop
    if string[i]=="" or string =='\n' or string == '\t': 
        count = count + 1    # count increase number in string

# prints the count of word in string
print("The number of word in String is:",count)
