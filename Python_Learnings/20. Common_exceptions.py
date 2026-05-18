# ValueError Example

try:
    age = int(input("Enter age: "))
    print(age)

except ValueError:
    print("Invalid input. Please enter numbers only")


# IndexError Example

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index out of range")
