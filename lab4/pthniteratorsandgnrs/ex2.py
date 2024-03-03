def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

def main():
    n = int(input("Enter the value of n: "))
    even_numbers = even_numbers_generator(n)
    print("Even numbers between 0 and", n, "are:", end=" ")
    print(*even_numbers, sep=", ")

if __name__ == "__main__":
    main()