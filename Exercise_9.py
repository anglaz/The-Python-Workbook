# Exercise 9: Compound Interest
# (19 Lines)
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

amount_in_account = float(input("How much money do you have?\n"))
i = 0
while i < 3:
    i+=1
    interest = amount_in_account * 0.04
    amount_in_account += interest
    print(f"You have {round(amount_in_account,2)} $ in your account after having accrued {round(interest,2)} $ in interest in year {i}")