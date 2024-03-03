ef trapezoid_area(base1, base2, height):
    return ((base1 + base2) * height) / 2


height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))


area = trapezoid_area(base1, base2, height)

print("Expected Output:", area)