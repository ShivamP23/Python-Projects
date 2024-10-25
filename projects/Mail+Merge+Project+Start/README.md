# Mail Merge Project

This project automates the process of creating personalized letters using Python. It reads a list of names and a letter template, replaces a placeholder in the template with each name, and generates individual letters for each person.

## How It Works

1. **Load Names**: The script reads names from `invited_names.txt`.
2. **Load Template**: It then reads the template letter from `starting_letter.txt`, which includes a placeholder `[name]`.
3. **Generate Personalized Letters**: For each name, the `[name]` placeholder in the template is replaced with the actual name, and the new letter is saved as a text file in the `ReadyToSend` folder.

The result is a set of customized letters ready for each recipient.
