# Exercise 3: Area of a Room
# (Solved—13 Lines)
# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

measurements_of_the_room = list(map(int, input("What is the width and length of this room?\n").split()))
print(measurements_of_the_room)
if len(measurements_of_the_room) > 2:
    print("You gave more than 2 measurements dummy")
else:
    area = measurements_of_the_room[0]*measurements_of_the_room[1]
    print(f"Your room has an area of {area} squared meters")