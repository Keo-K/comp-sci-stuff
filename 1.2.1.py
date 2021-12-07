import turtle  # imports
import random

wn = turtle.Screen()  # establishing the screen
wn.bgcolor("black")  # changing the background to be black because i can
default_spot_color = "red"  # setting a default spot color"
SPOT_SHAPE = "circle"  # setting constant variable circle, the shape will never change
FONT = ("Arial", 20, "normal")
default_spot_size = 5  # setting a default spot size value
score = 0  # very important user variable, used for keeping track of score
timer = 30  # very important variable, used for counting down the time and telling the user when the game is over
counting_interval = (
    1000  # the 1,000 represents 1 second, used in the counting down function
)
is_the_timer_up = (
    False  # used in the countdown function to determine if the timer is up
)
alternate_colors = [
    "blue",
    "green",
    "pink",
    "purple",
    "indigo",
    "yellow",
]  # setting alternate colors to change the spot to later
alternate_sizes = [
    x for x in range(1, 10)
]  # setting alternate sizes to change the spot for later
spot = turtle.Turtle()  # initializing the spot to click
spot.fillcolor(
    default_spot_color
)  # setting the spot's color value to the default color
spot.shape(SPOT_SHAPE)  # sets the spot's shape to the constant shape
spot.speed(1000)  # making the spot crazy fast
counter = (
    turtle.Turtle()
)  # initializes the counting turtle, the one that makes the countdown happen
counter.hideturtle()  # prevents the turtle from showing up, just the countdown text
counter.pu()  # makes it so no line is drawn upon moving
counter.goto(300, 300)  # sets up the counter position
counter.pd()  # lets the coutner draw again
counter.pencolor("white")  # changes the color of the countdown text
score_writer = (
    turtle.Turtle()
)  # initializes the turtle which will tell the user their score
score_writer.hideturtle()  # prevents the turtle from showing up, just the score text
score_writer.pu()  # makes it so no line is drawn upon moving
score_writer.goto(-300, 300)  # sets up the score writer position
score_writer.pd()  # allows the writer to write once more
score_writer.pencolor("white")  # changes the color of the score text


def countdown() -> None:
    global timer, is_the_timer_up  # allows global access to these variables
    counter.clear()  # clears the counter
    if timer <= 0:  # checks if the timer is currently at 0 or less
        counter.write("Time's up!", font=FONT)  # tells the user that their time is up
        is_the_timer_up = True  # sets the variable to True to signal the game is over
    else:
        counter.write(
            f"Timer: {timer}", font=FONT
        )  # if the timer is not up, it counts down towards 0
        timer -= 1  # subtracting one from the remaining time
        counter.getscreen().ontimer(countdown, counting_interval)


def update_score() -> None:
    global score  # allows access to the global score variable
    score += 1  # adds 1 to the total score
    score_writer.clear()  # tells the score writer to erase itself and get ready to write the next number
    score_writer.write(score, font=FONT)  # writes the users score to the screen


def change_spot_position() -> None:
    new_x_position = random.randint(-200, 200)  # sets a new x positional value
    new_y_position = random.randint(-200, 200)  # sets a new y positional value
    spot.hideturtle()  # hides the turtle temporarily
    spot.pu()  # tells the turtle not to draw a line
    spot.goto(
        new_x_position, new_y_position
    )  # moves the turtle to the new randomly generated positions
    spot.pd()  # says the turtle can draw lines again
    spot.showturtle()  # brings the turtle back to the user can see it again


def when_spot_is_clicked(x: int, y: int) -> None:
    global is_the_timer_up  # allows access to the global check if the timer is up
    if not is_the_timer_up:
        update_score()  # calls the above defined update_score() function if the timer is not up
        change_spot_position()  # calls the above defined change_spot_position() function
        _ = (
            alternate_colors.pop()
        )  # removes one value from the list of alternate colors and sets it to an unnamed variable
        spot.color(_)  # changes the color to the popped value
        _ = (
            alternate_sizes.pop()
        )  # removes a value from the list of alternate sizes and sets it to an unnamed variable
        spot.shapesize(_)  # changes the size to the size removed from the list
    else:
        spot.hideturtle()  # hides the spot when the timer is up


spot.onclick(
    when_spot_is_clicked
)  # event listener that tells the spot to do things when clicked
wn.ontimer(countdown, counting_interval)  # counts down
wn.mainloop()  # keeps the window open
