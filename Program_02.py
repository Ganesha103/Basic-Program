# Loop through numbers from 1 to 20
for i in range(1, 21):
    # Print spaces for pyramid alignment
    print(" " * (20 - i), end="")

    # Print numbers from 1 to i
    for num in range(1, i + 1):
        print(num, end=" ")

    print()  # Move to the next line
