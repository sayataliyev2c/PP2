def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Test the generator
def main():
    n = int(input("Enter the value of n: "))

    print(f"Counting down from {n} to 0:")
    for num in countdown(n):
        print(num)

if __name__ == "__main__":
    main()