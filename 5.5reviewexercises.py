num = float(input("Enter a number: "))
rounded_num = round(num, 2)
print(rounded_num)
print(f"{num} rounded to 2 decimal places is {rounded_num}")

num = float(input("Enter a number: "))
abs_num = float(abs(num))
print(f"The absolute value of {num} is {abs_num}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
Difference = num1 - num2
T_or_F = Difference.is_integer()
print(Difference.is_integer())
print(f"The difference bnetween {num1} and {num2} is an integer? {T_or_F}")
