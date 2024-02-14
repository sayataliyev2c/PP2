# Class for getString and printString methods
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())


# Shape class and its subclass Square
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Bank account class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted")
        else:
            print("Funds unavailable!")


# Function to filter prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Main program
if __name__ == "__main__":
    # Testing StringManipulator
    sm = StringManipulator()
    sm.getString()
    sm.printString()

    # Testing Square and Rectangle classes
    square = Square(5)
    print("Area of Square:", square.area())

    rectangle = Rectangle(4, 6)
    print("Area of Rectangle:", rectangle.area())

    # Testing Point class
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print("Distance between p1 and p2:", p1.dist(p2))

    # Testing Bank account class
    acc = Account("John")
    acc.deposit(100)
    acc.withdraw(50)
    acc.withdraw(70)

    # Filtering prime numbers in a list
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    prime_numbers = list(filter(lambda x: is_prime(x), numbers))
    print("Prime numbers in the list:", prime_numbers)