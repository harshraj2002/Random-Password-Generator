import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    #define character sets based on user preferences
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    #check if at least one character set is selected
    if not characters:
        return "No character sets selected. Please choose at least one."

    #generate a random password by sampling characters from the selected sets
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

try:
    password_length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters (y/n): ").strip().lower() == "y"
    use_lowercase = input("Include lowercase letters (y/n): ").strip().lower() == "y"
    use_digits = input("Include digits (y/n): ").strip().lower() == "y"
    use_special_chars = input("Include special characters (y/n): ").strip().lower() == "y"

    generated_password = generate_password(
        password_length, use_uppercase, use_lowercase, use_digits, use_special_chars
    )
    print(f"Generated Password: {generated_password}")
    
except ValueError:
    print("Please enter a valid integer for the password length.")

