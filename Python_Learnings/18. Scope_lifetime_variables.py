x = 100  # Global Variable

def display():
    y = 50  # Local Variable
    print("Inside Function - Local Variable:", y)
    print("Inside Function - Global Variable:", x)

display()

print("Outside Function - Global Variable:", x)
