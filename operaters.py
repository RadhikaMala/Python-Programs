# Take user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform all operations in a single line and print the result
print(f"Add: {num1} + {num2} = {num1 + num2}, Sub: {num1} - {num2} = {num1 - num2}, Mul: {num1} * {num2} = {num1 * num2}, Div: {num1} / {num2} = {num1 / num2 if num2 != 0 else 'undefined'}, Mod: {num1} % {num2} = {num1 % num2 if num2 != 0 else 'undefined'}, Exp: {num1} ** {num2} = {num1 ** num2}")
