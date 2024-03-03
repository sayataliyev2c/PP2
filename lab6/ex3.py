def is_palindrome(s):
  
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def main():
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

if __name__ == "__main__":
    main()