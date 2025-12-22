# Convert a string to an integer and test it
number_string = "5"
number_int = int(number_string)

result = number_int * 3
print(result)

# Convert a string to a floating-point number and test it
number_string = "2.5"
number_float = float(number_string)

result = number_float * 4
print(result)

# Display a string and an integer side-by-side using str()
text = "The number is"
number = 10

print(text + " " + str(number))

# Multiply two user-input numbers and display the result
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product = float(num1 * num2)

print(f"The product of {num1} and {num2} is {product}.")
