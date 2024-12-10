# Password Manager

A Python-based password manager with an integrated password generator. This tool enables you to create strong, secure passwords, store them, and retrieve them easily for various websites. It features a user-friendly graphical interface built using Tkinter.

## Features
- **Password Generator**: Generate secure, random passwords consisting of letters, numbers, and symbols.
- **Save Details**: Store website details, email/username, and passwords in a local JSON file for easy access.
- **Search Functionality**: Retrieve saved website login details (email and password) with the "Search" button.
- **User Interface**: A simple, intuitive GUI that makes it easy to interact with the password manager.

## How to Use
1. **Enter Website**: Type the website name (e.g., "example.com") in the "Website" field.
2. **Enter Email/Username**: Input the associated email or username for the account in the "Email/Username" field.
3. **Generate Password**: Click on the "Generate Password" button to create a random password with a combination of letters, numbers, and symbols.
4. **Save Details**: Click the "Add" button to securely save the website, email, and password in a JSON file.
5. **Search Passwords**: If you need to retrieve saved credentials, click the "Search" button and enter the website name.

## Notes
- The passwords are stored locally in a `data.json` file.
- The data is **not encrypted**. For enhanced security, consider implementing encryption.
- Make sure not to leave any fields empty when adding new data.
