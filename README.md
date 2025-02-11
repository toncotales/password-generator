# Password Generator
A Python script that generates strong, secure passwords. It creates password that adhere to modern security practices, ensuring strong randomness and complexity.

# Features
* __Strong Password Generation:__ Ensures no consecutive similar characters or character types.
* __Customizable:__ You can easily adjust the length and complexity of the generated password.
* __Security:__ Helps prevent weak passwords by avoiding common patterns and repetitive characters.

# Installation
You don't need to install any dependencies to run this script. Simply download or clone the repository and run the script directly.

## Clone the repository:
```bash
git clone https://github.com/toncotales/password-generator.git
```
## Run the script:
```bash
python password_generator.py
```

# Usage
## Example Usage:
```python
from password_generator import PasswordGenerator

pg = PasswordGenerator()
password = pg.generate(length=12)
print(password)
```
# Contributing
If you'd like to contribute to the project, feel free to fork the repository, create a branch, and submit a pull request with your changes. Contributions are always welcome!

# License
This project is licensed under the MIT License - see the <LICENSE> file for details.

# Author
Created by **Anthony Cotales**
