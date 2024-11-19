# program to check given string is Palindrome or not
String_1 = input("Enter the string:")
String_2 ="" # Creating string
for i in String_1:  # Checking string
    String_2 = i + String_1  # If string present increment
if String_1 == String_2:
    print("The given string is Palindrome",True)
else:
    print("The given string is not Palindrome",False)
