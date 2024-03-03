def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

def main():
    filename = input("Enter the name of the file to write: ")
    data = input("Enter the list items separated by space: ").split()

    write_list_to_file(filename, data)
    print(f"List has been written to '{filename}'.")

if __name__ == "__main__":
    main()