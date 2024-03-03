import os

def list_directories_files(path, directories_only=False):
    
    all_entries = os.listdir(path)
    directories = [entry for entry in all_entries if os.path.isdir(os.path.join(path, entry))]
    files = [entry for entry in all_entries if os.path.isfile(os.path.join(path, entry))]
    
    if directories_only:
        return directories
    else:
        return directories, files

def main():
    path = input("Enter the path: ")

    print("\nDirectories:")
    directories = list_directories_files(path, directories_only=True)
    for directory in directories:
        print(directory)

    print("\nFiles:")
    directories, files = list_directories_files(path)
    for file in files:
        print(file)

    print("\nAll directories and files:")
    all_entries = list_directories_files(path)
    for entry in all_entries:
        print(entry)

if __name__ == "__main__":
    main()