import turtle
import random

# imports

START_POS = (-400, 400)  # start position, constant variable
PATH_WIDTH = 20  # constant space between each line
line_distance = 800

window = turtle.Screen()  # window object
window.bgcolor("black")

maze = turtle.Turtle()  # maze drawing turtle
maze.pu()  # picks up the pen
maze.speed(10)  # makes him fast
maze.goto(START_POS)  # moves to the start position
maze.pd()  # puts the pen down
maze.pensize(5)  # changes thickness of the pen
maze.pencolor("red")


def random_bool() -> bool:
    return random.choice([True, False])


def random_distance(upper_bound: int) -> int:
    if upper_bound <= 0:
        return 1
    return random.randint(1, upper_bound)


for y in range(40):
    quarter_dist = int(line_distance / 4) if line_distance != 0 else 1
    if random_bool():
        distance = random_distance(quarter_dist * 2)
        half = quarter_dist * 2
        full = quarter_dist * 4
        maze.forward(half - distance)
        if random_bool() and quarter_dist >= 50 and quarter_dist <= 150:
            maze.right(90)
            maze.forward(PATH_WIDTH * 2)
            maze.backward(PATH_WIDTH * 2)
            maze.left(90)
        maze.pu()
        maze.forward(distance)
        maze.pd()
        maze.forward(half)
    else:
        maze.forward(quarter_dist * 4)
    line_distance -= 20
    maze.right(90)
maze.hideturtle()

window.mainloop()  # keeping the window open
