# Random Password Generator

A secure, user-friendly Python application that generates cryptographically strong passwords with customizable options. This tool uses Python's `secrets` module to ensure maximum security and unpredictability in password generation.

## Features

### 🔐 Security Features
- **Cryptographically Secure**: Uses Python's `secrets` module instead of `random` for true randomness
- **Pattern Detection**: Automatically detects and prevents predictable patterns
- **Anti-Sequential Protection**: Prevents sequential characters (e.g., "abc", "123")
- **No Repeated Patterns**: Avoids excessive repetition of identical characters
- **Guaranteed Diversity**: Ensures at least one character from each selected character type

### 🎯 User Features
- **Customizable Length**: Set password length (minimum 4 characters)
- **Character Type Selection**: Choose from uppercase, lowercase, numbers, and special characters
- **Batch Generation**: Generate multiple passwords at once
- **File Export**: Save generated passwords to a text file
- **Interactive Interface**: User-friendly command-line interface with clear prompts
- **Input Validation**: Robust error handling and input validation

### 🛡️ Security Standards
- No predictable patterns or sequences
- Cryptographically secure random number generation
- Protection against common password attack vectors
- Compliance with modern password security best practices

## Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

### Setup
1. Clone or download the project files
2. Ensure Python is installed on your system
3. No additional installation required

## Usage

### Running the Application
```
python password_generator.py
```

### Interactive Mode
The application will guide you through the following options:

1. **Password Length**: Enter desired length (minimum 4 characters)
2. **Character Types**: Select which character types to include:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Numbers (0-9)
   - Special characters (!@#$%^&*()_+-=[]{}|;:,.<>?)
3. **Quantity**: Specify how many passwords to generate
4. **File Export**: Option to save passwords to a text file

### Example Session
```
==================================================
    SECURE RANDOM PASSWORD GENERATOR
==================================================
Enter password length (minimum 4): 16
Select character types to include:
Include uppercase letters? (Y/n): Y
Include lowercase letters? (Y/n): Y
Include numbers? (Y/n): Y
Include special characters? (Y/n): Y
How many passwords to generate? (default 1): 3
Save passwords to file? (y/N): y
Enter filename (press Enter for 'generated_passwords.txt'): my_passwords.txt

Generating secure passwords...

==================================================
    GENERATED PASSWORDS
==================================================
Password 1: K9$mP2vX@nL4qR7!
Password 2: 8#bY5wN*zT1aE6&j
Password 3: F3!rU9@sM7#pQ2%k
==================================================

Passwords successfully saved to 'my_passwords.txt'
```

## Code Structure

### Main Components

- **`SecurePasswordGenerator` Class**: Core password generation logic
- **`generate_password()`**: Creates individual secure passwords
- **`generate_multiple_passwords()`**: Batch password generation
- **`_has_predictable_patterns()`**: Pattern detection and validation
- **`save_passwords_to_file()`**: File export functionality
- **`get_user_input()`**: Interactive user interface
- **`display_passwords()`**: Formatted password display
- **`main()`**: Application entry point and flow control

### Key Methods

#### `generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)`
Generates a single secure password with specified criteria.

**Parameters:**
- `length` (int): Password length (minimum 4)
- `use_uppercase` (bool): Include uppercase letters
- `use_lowercase` (bool): Include lowercase letters
- `use_digits` (bool): Include numbers
- `use_special` (bool): Include special characters

**Returns:** Secure password string

#### `generate_multiple_passwords(count, **kwargs)`
Generates multiple passwords with the same criteria.

**Parameters:**
- `count` (int): Number of passwords to generate
- `**kwargs`: Password generation parameters

**Returns:** List of generated passwords

## Security Implementation

### Cryptographic Security
- Uses `secrets.choice()` for character selection
- Uses `secrets.SystemRandom().shuffle()` for password shuffling
- No pseudorandom number generators that could be predictable

### Pattern Detection
The application automatically detects and prevents:
- Sequential characters (3+ in a row): "abc", "123", "xyz"
- Repeated characters (3+ identical): "aaa", "111"
- Common keyboard patterns: "qwe", "asd", "zxc"

### Character Requirements
- Ensures at least one character from each selected character type
- Shuffles final password to avoid predictable positioning
- Validates minimum length requirements

## File Operations

### Saving Passwords
Generated passwords can be saved to a text file with the following format:
```
Generated Secure Passwords
==============================

Password 1: K9$mP2vX@nL4qR7!
Password 2: 8#bY5wN*zT1aE6&j
Password 3: F3!rU9@sM7#pQ2%k
```

### Default Filename
If no filename is specified, passwords are saved to `generated_passwords.txt`

## Best Practices

### Password Security
- Use passwords at least 12 characters long for better security
- Include all character types (uppercase, lowercase, numbers, special characters)
- Generate unique passwords for each account or service
- Store passwords securely using a password manager

### Usage Recommendations
- Don't share generated passwords over unsecured channels
- Consider generating multiple options and selecting the most suitable
- Regularly update passwords, especially for sensitive accounts

## Error Handling

The application includes comprehensive error handling for:
- Invalid input validation
- File operation errors
- Character type selection validation
- Password length constraints
- Pattern detection and regeneration

## Technical Requirements

### System Requirements
- **Python Version**: 3.6+
- **Operating System**: Cross-platform (Windows, macOS, Linux)
- **Memory**: Minimal memory footprint
- **Storage**: No persistent storage required (except for optional file export)

### Dependencies
- `secrets` - Cryptographically secure random number generation
- `string` - Character set definitions
- `re` - Regular expression pattern matching
- `os` - File system operations
- `typing` - Type hints for better code clarity

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate tests
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Include comprehensive docstrings
- Add type hints where appropriate
- Maintain backward compatibility

## License

This project is open source and available under the MIT License.

## Author

Harsh Raj
