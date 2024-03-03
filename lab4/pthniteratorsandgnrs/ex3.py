def divisible_by_three_and_four_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


def main():
    n = int(input("Enter the value of n: "))
    generator = divisible_by_three_and_four_generator(n)
    print("Numbers between 0 and", n, "divisible by both 3 and 4 are:")
    for num in generator:
        print(num, end=", ")

if __name__ == "__main__":
    main()