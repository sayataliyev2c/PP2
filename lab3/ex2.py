# Function to convert grams to ounces
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Function to solve the puzzle of counting chickens and rabbits
def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens
        if (2 * num_chickens) + (4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits
    return "No solution found"

# Function to filter prime numbers from a list
def filter_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = list(filter(lambda x: is_prime(x), numbers.split()))
    return prime_numbers

# Function to print all permutations of a string
def print_permutations(string):
    from itertools import permutations
    perms = permutations(string)
    for perm in perms:
        print(''.join(perm))

# Function to reverse words in a sentence
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Function to check if a list contains a 3 next to a 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Function to check if a list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 0

# Function to compute the volume of a sphere
def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * (radius ** 3)
    return volume

# Function to return unique elements of a list
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Function to check if a word or phrase is a palindrome
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

# Function to print histogram
def histogram(numbers):
    for num in numbers:
        print('*' * num)

# Function to play the "Guess the number" game
def guess_the_number():
    import random
    number_to_guess = random.randint(1, 20)
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

# Test the functions
def main():
    print(grams_to_ounces(100))
    print(fahrenheit_to_celsius(68))
    print(solve(35, 94))
    [1,]
    print(filter_prime("2 3 4 5 6 7 8 9 10 11 12 13 14 15"))
    print_permutations("abc")
    print(reverse_sentence("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1,2,4,0,0,7,5]))
    print(sphere_volume(5))
    print(unique_elements([1, 2, 3, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])
    guess_the_number()

if __name__ == "__main__":
    main()