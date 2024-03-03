import os

def get_filename_and_directory(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return None, None

def main():
    path = input("Enter the path to test: ")
    filename, directory = get_filename_and_directory(path)

    if filename and directory:
        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print("The specified path does not exist.")

if __name__ == "__main__":
    main()