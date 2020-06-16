# Exercise 4: Area of a Field
# (Solved—15 Lines)
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

measurements_of_the_field = list(map(int, input("What is the width and length of your field in meters?\n").split()))
if len(measurements_of_the_field) > 2:
    print("You gave more than 2 measurements dummy")
else:
    area = float((measurements_of_the_field[0]*measurements_of_the_field[1])/4046)
    print(f"Your room has an area of {area} acres")

