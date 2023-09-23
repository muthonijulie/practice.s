# Program to demonstrate operator precedence in Python

a = 5
b = 3
c = 2

# Arithmetic operations
result = a + b * c  # Multiplication has higher precedence than addition
print("Result of a + b * c =", result)  # Output: 11

# Parentheses can be used to override precedence
result = (a + b) * c  # Addition has higher precedence due to parentheses
print("Result of (a + b) * c =", result)  # Output: 16

# Comparison operations
result = a > b + c  # Addition has higher precedence than comparison
print("Result of a > b + c =", result)  # Output: False

# Logical operations
p = True
q = False
r = True

result = p or q and r  # Logical AND has higher precedence than logical OR
print("Result of p or q and r =", result)  # Output: True

# Assignment operations
x = 10
y = 5

x += y * c  #Multiplication has a higher precedence than addition
print("Value of x after x += y * c is", x)  # Output: 20
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
