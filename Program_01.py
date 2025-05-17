# Input string
text = "GUVI Geeks Network Private Limited"

# Convert text to uppercase for case-insensitive counting
text_upper = text.upper()

# Vowel characters to check
vowels = "AEIOU"

# Initialize vowel counts dictionary
vowel_counts = {v: text_upper.count(v) for v in vowels}

# Calculate total vowels
total_vowels = sum(vowel_counts.values())

# Display results
print(f"Total vowels: {total_vowels}")
for vowel, count in vowel_counts.items():
    print(f"{vowel}: {count}")
