from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
my_screen = Screen()
print(my_screen.canvheight)
timmy.shape("turtle")
timmy.color("red")
timmy.turtlesize(10, 10, 12)
timmy.forward(100)

my_screen.exitonclick()

x = PrettyTable()

x.field_names = ["Name:", "Penis Size", "Hotness"]
x.add_rows(
    [
        ["Devin", 10, 10],
        ["Ed", 2, 2],
        ["Callum", 1, 7],
    ]
)

print(x)