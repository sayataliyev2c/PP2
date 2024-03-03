import os

def check_path_access(path):
   
    if not os.path.exists(path):
        print("Specified path does not exist.")
        return

    
    if not os.access(path, os.R_OK):
        print("Specified path is not readable.")
    else:
        print("Specified path is readable.")

    
    if not os.access(path, os.W_OK):
        print("Specified path is not writable.")
    else:
        print("Specified path is writable.")

    if not os.access(path, os.X_OK):
        print("Specified path is not executable.")
    else:
        print("Specified path is executable.")

def main():
    path = input("Enter the path to check access: ")
    check_path_access(path)

if __name__ == "__main__":
    main()