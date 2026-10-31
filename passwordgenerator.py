
import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):

    characters = ""
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        return "Please select at least one character type."

    if length < len(password):
        return "Password length is too short for selected options."

    # Fill the remaining password length
    for i in range(length - len(password)):
        password.append(secrets.choice(characters))

    # Shuffle characters to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

if length <= 0:
    print("Password length must be greater than zero.")

else:
    password = generate_password(
        length,
        use_upper,
        use_lower,
        use_digits,
        use_symbols
    )

    print("\nGenerated Password:", password)
