import os

def check_path_access(path):
    if os.path.exists(path):
        if os.access(path, os.F_OK):
            return True
        else:
            print("No access to the specified path.")
            return False
    else:
        print("Specified path does not exist.")
        return False

def delete_file(path):
    if check_path_access(path):
        try:
            os.remove(path)
            print("File deleted successfully.")
        except PermissionError:
            print("Permission denied to delete the file.")
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Cannot delete the file.")

def main():
    path = input("Enter the path of the file to delete: ")
    delete_file(path)

if __name__ == "__main__":
    main()