# Exercise 8: Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

widgets_number = int(input("Number of widgets?\n"))
gizmos_number = int(input("Number of widgets?\n"))
print(f"the total weight is {widgets_number * 75 + gizmos_number * 112} grams")