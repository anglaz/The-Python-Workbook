# Exercise 7: Sum of the First n Positive Integers
# (Solved—12 Lines)
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula: sum = ((n)(n + 1))/2

n_value = int(input("Value of n?\n"))
sum_n = int(((n_value) * (n_value + 1)) / 2)
print(f"The sum of the numbers from 1 to {n_value} is {sum_n}")