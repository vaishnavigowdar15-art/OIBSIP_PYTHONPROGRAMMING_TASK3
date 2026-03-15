import random
import string

print("Password Generator")

# Ask user for password length
length = int(input("Enter password length: "))

# Ask user for character preferences
use_letters = input("Include letters? (y/n): ")
use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

characters = ""

# Add characters based on user choice
if use_letters == 'y':
    characters += string.ascii_letters

if use_numbers == 'y':
    characters += string.digits

if use_symbols == 'y':
    characters += string.punctuation

# Check if user selected at least one option
if characters == "":
    print("You must select at least one character type!")
else:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)
