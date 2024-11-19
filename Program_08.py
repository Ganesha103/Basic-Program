# program to find Anagrams from strings
string_1 = input("Enter 1 string:")
string_2 = input("Enter 2 string:")

if sorted(string_1) == sorted(string_2): # sorting string and Checking are equal or not
    print(" The strings are anagrams :",True)
else:
    print(" The strings are anagrams :",False)
