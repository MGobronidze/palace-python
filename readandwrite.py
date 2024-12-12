# File Handling in Python: A Project for Learning

# This project covers:
# 1. Reading from and writing to files
# 2. Working with file modes
# 3. Handling exceptions
def read_file(file_path):
    """Reads the content of a file and prints it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print("File Content:")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def write_to_file(file_path, content):
    """Writes the provided content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
            print(f"Content successfully written to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def append_to_file(file_path, content):
    """Appends the provided content to a file."""
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(content)
            print(f"Content successfully appended to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")


def file_handling_demo():
    """Demonstrates file handling with different modes and exception handling."""
    demo_file = 'demo.txt'

    print("\n1. Writing to a file:")
    write_to_file(demo_file, "Hello, this is a demo file.\n")

    print("\n2. Appending to the file:")
    append_to_file(demo_file, "This is additional content.\n")

    print("\n3. Reading the file:")
    read_file(demo_file)

    print("\n4. Handling errors:")
    non_existent_file = 'non_existent.txt'
    read_file(non_existent_file)
    
    print("\n1. Writing to a file:")
    write_to_file(demo_file, "new data.\n")
    

if __name__ == "__main__":
    file_handling_demo()
