"""
PROJECT 3: RANDOM PASSWORD GENERATOR
DecodeLabs - Python Programming Internship
"""

import random
import string

print("=" * 45)
print("          RANDOM PASSWORD GENERATOR")
print("=" * 45)

print("\nGenerate a strong password using letters and numbers.")

while True:
    try:
        length = int(input("\nEnter password length: "))

        if length < 2:
            print("Password length must be at least 2 characters.")
            continue

        break

    except ValueError:
        print("Invalid input! Please enter a whole number.")

# Character sets
letters = string.ascii_letters
digits = string.digits

# Combine letters and numbers
all_characters = letters + digits

# Use a secure random number generator
secure_random = random.SystemRandom()

# Ensure at least one letter and one number
password = [
    secure_random.choice(letters),
    secure_random.choice(digits)
]

# Generate the remaining characters
for i in range(length - 2):
    password.append(secure_random.choice(all_characters))

# Shuffle characters to make their positions unpredictable
secure_random.shuffle(password)

# Convert the list into a single password string
generated_password = "".join(password)

# Display the generated password
print("\n" + "=" * 45)
print("           PASSWORD GENERATED!")
print("=" * 45)

print("\nYour Password:", generated_password)
print("Password Length:", len(generated_password), "characters")
print("Contains Letters: Yes")
print("Contains Numbers: Yes")

print("\n" + "=" * 45)
print("Thank you for using Password Generator!")
print("=" * 45)