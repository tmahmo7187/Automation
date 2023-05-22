import os

# File path
file_path = 'file.txt'

# Method 1: Writing to a file
phrases = ['Phrase 1', 'Phrase 2', 'Phrase 3']
with open(file_path, 'w') as file:
    # Iterate over the phrases and write each one to a new line in the file
    for phrase in phrases:
        file.write(phrase + '\n')

# Method 2: Appending to a file
new_phrases = ['Phrase 4', 'Phrase 5']
with open(file_path, 'a') as file:
    # Iterate over the new phrases and append each one to a new line in the file
    for phrase in new_phrases:
        file.write(phrase + '\n')

# Method 3: Reading from a file
with open(file_path, 'r') as file:
    # Read the entire contents of the file
    contents = file.read()
    print(contents)

# Method 4: Reading file line by line
with open(file_path, 'r') as file:
    # Read the file line by line
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Use strip() to remove newline characters

# Method 5: Checking if a file exists
if os.path.exists(file_path):
    print("File exists!")
else:
    print("File does not exist.")

# Method 6: Renaming a file
new_file_path = 'new_file.txt'
os.rename(file_path, new_file_path)

# Method 7: Deleting a file
if os.path.exists(new_file_path):
    os.remove(new_file_path)
    print("File deleted!")
else:
    print("File not found.")
