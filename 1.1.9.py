import random, string, turtle, colorsys

hex_gen = list(string.ascii_uppercase[:6]) + [str(x) for x in range(0, 10)]
"""
The list above is generated using the letters ABCDEF and the numbers from 0 to 9
this is just essentially the same as 
["A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
"""


def get_hsv(hexrgb: str) -> tuple:
    """
    removes any hashtags because i made the hex values have #'s in order
    to be more readable
    converts the hex code into an hsv in order to sort by hue
    """
    hexrgb = hexrgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(hexrgb[i : i + 2], 16) / 255.0 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)  # returns hsv conversion


x = ["#" + "".join([random.choice(hex_gen) for x in range(6)]) for x in range(360)]
"""
above list is randomly generated hex values, preceded by a #
"""

x.sort(key=get_hsv)
"""
sorts by the key given by the hex to hsv code in order to sort by hue
"""
print(x)  # for debugging

wn = turtle.Screen()  # makees the screen
wn.bgcolor("black")  # changes the color to black
t = turtle.Turtle()  # creates the main turtle
while True:  # infinite loop
    t.pensize(5)  # changes pensize
    t.speed(100)  # sets the speed to 100
    t.hideturtle()  # makes the turtle invisible
    for i in range(360):  # does this 360 times
        if i % 60 == 0:  # every loop of 60, clear the screen
            t.clear()
        t.pu()  # do penup between squares
        t.goto(random.randint(-700, 700), random.randint(-400, 300))  # changes position
        t.pd()  # puts pendown
        t.right(random.randint(1, 60))  # turns right by one unit
        t.color(x[i])  # changes the color to be the next color in the sorted list
        t.circle(
            random.randint(1, 90), 360, random.choice([360, 3, 4])
        )  # draws the circle (square) with a randomized size
wn.mainloop()  # the main loop
