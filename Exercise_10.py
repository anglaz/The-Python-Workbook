# Exercise 10: Arithmetic
# (Solved—20 Lines)
# Create a program that reads two integers, a and b, from the user. Your program should compute and display:
#• The sum of a and b
#• The difference when b is subtracted from a
#• The product of a and b
#• The quotient when a is divided by b
#• The remainder when a is divided by b
#• The result of log10 a
#• The result of a^b

import math

int_a = int(input("Number a?\n"))
int_b = int(input("Number b?\n"))
print(f"The sum of a and b is {int_a + int_b}")
print(f"The difference when b is subtracted from a is {int_a - int_b}")
print(f"The product of a and b is {int_a * int_b}")
print(f"The quotient when a is divided by b is {int_a / int_b}")
print(f"The remainder when a is divided by b is {int_a % int_b}")
print(f"The result of log10 a is {math.log10(int_a)}")
print(f"The result of a^b is {int_a ** int_b}")