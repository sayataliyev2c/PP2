import string

def generate_text_files():
    for char in string.ascii_uppercase:
        filename = char + ".txt"
        with open(filename, 'w') as file:
            file.write(f"This is {filename}.\n")

def main():
    generate_text_files()
    print("Text files A.txt to Z.txt have been generated.")

if __name__ == "__main__":
    main()