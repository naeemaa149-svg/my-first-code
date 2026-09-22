# Calculate the average (arithmetic mean) of three numbers

# Get three numbers from the user
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

# Calculate total and average (rounded to 2 decimal places)
total = x + y + z
arithmetic = round(total / 3, 2)

# Output the result
print(f"Arithmetic Mean = {arithmetic}")
