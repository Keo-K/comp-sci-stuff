#   a123_apple_1.py
import turtle
import string
import random

# -----setup-----
apple_image = "apple.gif"  # Store the file name of your shape
FONT = ("Arial", 20, "normal")
wn = turtle.Screen()
wn.screensize(300, 200)
wn.bgpic("background.gif")
wn.addshape(apple_image)  # Make the screen aware of the new file


# -----functions-----
# given a turtle, set that turtle to be shaped by the image file
hashmap = {
    random.choice(list(string.ascii_uppercase)): {
        "turtle": turtle.Turtle(),
        "writer": turtle.Turtle(),
    }
    for i in range(5)
}

n = -200

for apple in hashmap:
    appl = hashmap[apple]["turtle"]
    writer = hashmap[apple]["writer"]
    writer.pu()
    writer.hideturtle()
    appl.hideturtle()
    appl.shape(apple_image)
    appl.pu()
    appl.speed(20)
    appl.goto(n, 100)
    writer.goto(n, 100 - 20)
    writer.pencolor("white")
    writer.write(apple, font=FONT, align="center")
    appl.showturtle()
    n += 100


# -----function calls-----
for j in hashmap:
    wn.onkeypress(
        (
            lambda h=hashmap[j]: h["turtle"].right(90)
            or h["turtle"].speed(10)
            or h["turtle"].forward(800)
            or h["writer"].clear()
        ),
        j.lower(),
    )
    wn.listen()

wn.mainloop()
