from functools import reduce

def multiply_list(numbers):
    
    result = reduce(lambda x, y: x * y, numbers)
    return result

def main():
   
    numbers = [2, 3, 4, 5]

   
    result = multiply_list(numbers)

    print("List:", numbers)
    print("Result of multiplying all numbers:", result)

if __name__ == "__main__":
    main()