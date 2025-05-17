# Take input strings from the user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Get the lengths of both strings
m, n = len(str1), len(str2)

# Initialize a table to store common substring lengths
dp = [[0] * (n + 1) for _ in range(m + 1)]
longest_length = 0
end_index = 0  # Stores the ending index of the longest common substring in str1

# Find the longest common substring
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:  # Matching characters
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > longest_length:
                longest_length = dp[i][j]
                end_index = i
        else:
            dp[i][j] = 0  # Reset for non-matching characters

# Extract the longest common substring
longest_substring = str1[end_index - longest_length:end_index]

# Print the result
print(f"Longest Common Substring: '{longest_substring}'")
