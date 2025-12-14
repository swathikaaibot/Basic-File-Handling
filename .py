# Find and Replace Words

def read_file(file_name):
    """Read the contents of a file"""
    try:
        with open(file_name, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_file(file_name, data):
    """Write data to a file"""
    try:
        with open(file_name, "w") as file:
            file.write(data)
        print(f"Data successfully saved to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_and_replace(file_name, old_word, new_word):
    """Find and replace a word in the file"""
    data = read_file(file_name)
    if data:
        if old_word in data:
            new_data = data.replace(old_word, new_word)
            write_file(file_name, new_data)
        else:
            print(f"The word '{old_word}' was not found in the file.")

# --- Main Program ---
file_name = input("Enter the file name (with extension): ")
old_word = input("Enter the word to find: ")
new_word = input("Enter the new word to replace it with: ")

find_and_replace(file_name, old_word, new_word)
