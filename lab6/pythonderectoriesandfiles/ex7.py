def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                for line in source:
                    destination.write(line)
        print("File copied successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()