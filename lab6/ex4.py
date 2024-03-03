import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000) 
    square_root = math.sqrt(number)
    return square_root

def main():
    number = int(input("Enter the number: "))
    milliseconds = int(input("Enter the milliseconds to wait: "))

    result = delayed_square_root(number, milliseconds)

    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

if __name__ == "__main__":
    main()