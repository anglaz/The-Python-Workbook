# Exercise 12: Distance Between Two Points on Earth
# (27 Lines)
# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

import math
p1 = list(map(int, input("latitud y longitud del punto 1: ").split()))
if len(p1) > 2:
    print("Wrong format")
    exit
p2 = list(map(int, input("latitud y longitud del punto 2: ").split()))
if len(p2) > 2:
    print("Wrong format")
    exit
print(p1, p2)
