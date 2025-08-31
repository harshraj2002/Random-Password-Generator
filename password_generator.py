"""
Random Password Generator
A secure password generator that creates cryptographically strong passwords
using Python's secrets module for maximum security.
"""

import secrets
import string
import re
import os
from typing import List, Set


class SecurePasswordGenerator:
    """A class to generate secure, random passwords with customizable options."""
    
    def __init__(self):
        """Initialize the password generator with character sets."""
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
    def generate_password(self, length: int = 12, 
                         use_uppercase: bool = True,
                         use_lowercase: bool = True,
                         use_digits: bool = True,
                         use_special: bool = True) -> str:
        """
        Generate a single secure password with specified criteria.
        
        Args:
            length (int): Length of the password (minimum 4)
            use_uppercase (bool): Include uppercase letters
            use_lowercase (bool): Include lowercase letters
            use_digits (bool): Include numbers
            use_special (bool): Include special characters
            
        Returns:
            str: Generated secure password
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character pool based on user preferences
        char_pool = ""
        required_chars = []
        
        if use_lowercase:
            char_pool += self.lowercase
            required_chars.append(secrets.choice(self.lowercase))
            
        if use_uppercase:
            char_pool += self.uppercase
            required_chars.append(secrets.choice(self.uppercase))
            
        if use_digits:
            char_pool += self.digits
            required_chars.append(secrets.choice(self.digits))
            
        if use_special:
            char_pool += self.special_chars
            required_chars.append(secrets.choice(self.special_chars))
        
        if not char_pool:
            raise ValueError("At least one character type must be selected")
        
        # Generate password ensuring at least one character from each selected type
        password = required_chars.copy()
        
        # Fill remaining length with random characters from the pool
        for _ in range(length - len(required_chars)):
            password.append(secrets.choice(char_pool))
        
        # Shuffle the password to avoid predictable patterns
        secrets.SystemRandom().shuffle(password)
        
        # Convert to string and validate
        final_password = ''.join(password)
        
        # Ensure no predictable patterns
        if self._has_predictable_patterns(final_password):
            # Regenerate if patterns are detected (recursive call)
            return self.generate_password(length, use_uppercase, use_lowercase, 
                                        use_digits, use_special)
        
        return final_password
    
    def _has_predictable_patterns(self, password: str) -> bool:
        """
        Check if password contains predictable patterns.
        
        Args:
            password (str): Password to check
            
        Returns:
            bool: True if predictable patterns are found
        """
        # Check for sequential characters (3 or more in a row)
        for i in range(len(password) - 2):
            if (ord(password[i+1]) == ord(password[i]) + 1 and 
                ord(password[i+2]) == ord(password[i]) + 2):
                return True
                
        # Check for repeated characters (3 or more identical consecutive chars)
        if re.search(r'(.)\1{2,}', password):
            return True
            
        # Check for common patterns
        common_patterns = ['123', '321', 'abc', 'cba', 'qwe', 'asd', 'zxc']
        password_lower = password.lower()
        for pattern in common_patterns:
            if pattern in password_lower:
                return True
                
        return False
    
    def generate_multiple_passwords(self, count: int, **kwargs) -> List[str]:
        """
        Generate multiple passwords with the same criteria.
        
        Args:
            count (int): Number of passwords to generate
            **kwargs: Password generation parameters
            
        Returns:
            List[str]: List of generated passwords
        """
        if count < 1:
            raise ValueError("Count must be at least 1")
            
        passwords = []
        for _ in range(count):
            passwords.append(self.generate_password(**kwargs))
            
        return passwords
    
    def save_passwords_to_file(self, passwords: List[str], filename: str = None):
        """
        Save generated passwords to a text file.
        
        Args:
            passwords (List[str]): List of passwords to save
            filename (str, optional): Name of the file to save to
        """
        if filename is None:
            filename = "generated_passwords.txt"
            
        try:
            with open(filename, 'w') as file:
                file.write("Generated Secure Passwords\n")
                file.write("=" * 30 + "\n\n")
                for i, password in enumerate(passwords, 1):
                    file.write(f"Password {i}: {password}\n")
                    
            print(f"Passwords successfully saved to '{filename}'")
            
        except IOError as e:
            print(f"Error saving passwords to file: {e}")


def get_user_input():
    """
    Get user preferences for password generation.
    
    Returns:
        dict: Dictionary containing user preferences
    """
    print("=" * 50)
    print("    SECURE RANDOM PASSWORD GENERATOR")
    print("=" * 50)
    
    # Get password length
    while True:
        try:
            length = int(input("Enter password length (minimum 4): "))
            if length >= 4:
                break
            else:
                print("Password length must be at least 4 characters.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get character type preferences
    print("\nSelect character types to include:")
    use_uppercase = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    use_lowercase = input("Include lowercase letters? (Y/n): ").lower() != 'n'
    use_digits = input("Include numbers? (Y/n): ").lower() != 'n'
    use_special = input("Include special characters? (Y/n): ").lower() != 'n'
    
    # Validate at least one type is selected
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        print("At least one character type must be selected. Using all types.")
        use_uppercase = use_lowercase = use_digits = use_special = True
    
    # Get number of passwords
    while True:
        try:
            count = int(input("How many passwords to generate? (default 1): ") or "1")
            if count >= 1:
                break
            else:
                print("Number of passwords must be at least 1.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Ask about saving to file
    save_to_file = input("Save passwords to file? (y/N): ").lower() == 'y'
    filename = None
    if save_to_file:
        filename = input("Enter filename (press Enter for 'generated_passwords.txt'): ").strip()
        if not filename:
            filename = "generated_passwords.txt"
    
    return {
        'length': length,
        'use_uppercase': use_uppercase,
        'use_lowercase': use_lowercase,
        'use_digits': use_digits,
        'use_special': use_special,
        'count': count,
        'save_to_file': save_to_file,
        'filename': filename
    }


def display_passwords(passwords: List[str]):
    """
    Display generated passwords in a formatted manner.
    
    Args:
        passwords (List[str]): List of passwords to display
    """
    print("\n" + "=" * 50)
    print("    GENERATED PASSWORDS")
    print("=" * 50)
    
    for i, password in enumerate(passwords, 1):
        print(f"Password {i}: {password}")
    
    print("=" * 50)


def main():
    """Main function to run the password generator."""
    try:
        # Initialize the password generator
        generator = SecurePasswordGenerator()
        
        while True:
            # Get user preferences
            preferences = get_user_input()
            
            # Generate passwords
            print("\nGenerating secure passwords...")
            passwords = generator.generate_multiple_passwords(
                count=preferences['count'],
                length=preferences['length'],
                use_uppercase=preferences['use_uppercase'],
                use_lowercase=preferences['use_lowercase'],
                use_digits=preferences['use_digits'],
                use_special=preferences['use_special']
            )
            
            # Display passwords
            display_passwords(passwords)
            
            # Save to file if requested
            if preferences['save_to_file']:
                generator.save_passwords_to_file(passwords, preferences['filename'])
            
            # Ask if user wants to generate more passwords
            print("\nWould you like to generate more passwords?")
            continue_choice = input("Enter 'y' to continue or any other key to exit: ").lower()
            
            if continue_choice != 'y':
                print("\nThank you for using the Secure Random Password Generator!")
                break
                
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
