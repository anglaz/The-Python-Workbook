# Exercise 11: Fuel Efficiency
# (13 Lines)
# In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). In Canada, fuel efficiency 
# is normally expressed in liters-per-hundred kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.

mpg = int(input("Miles per gallon?\n"))
print(f"That would be {mpg * 235.215} L/100 km")