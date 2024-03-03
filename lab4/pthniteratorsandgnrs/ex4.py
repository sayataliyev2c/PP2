def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


def main():
    a = int(input("Enter the starting value (a): "))
    b = int(input("Enter the ending value (b): "))

    print(f"Squares of numbers from {a} to {b}:")
    for square in squares(a, b):
        print(square)

if __name__ == "__main__":
    main()