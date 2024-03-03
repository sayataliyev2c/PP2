def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return None

def main():
    filename = input("Enter the name of the text file: ")
    line_count = count_lines(filename)
    
    if line_count is not None:
        print(f"Number of lines in '{filename}': {line_count}")

if __name__ == "__main__":
    main()