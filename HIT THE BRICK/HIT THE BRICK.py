# Importing the only library required
import turtle

# Creating the screen for the game
SCREEN = turtle.Screen()
SCREEN.title("PONG PONG")
SCREEN.bgcolor("black")
SCREEN.setup(width = 800, height = 600)
SCREEN.tracer(0)

# Score bars
SCORE_A = 0
SCORE_B = 0

# The main two bars by which you will be able to hit the random ball
# PADDLE A
PADDLE_A = turtle.Turtle()
PADDLE_A.speed(0)
PADDLE_A.shape("square")
PADDLE_A.color("white")
PADDLE_A.shapesize(stretch_wid = 5, stretch_len = 0.5)
PADDLE_A.penup()
PADDLE_A.goto(-360, 0)

# PADDLE B
PADDLE_B = turtle.Turtle()
PADDLE_B.speed(5)
PADDLE_B.shape("square")
PADDLE_B.color("white")
PADDLE_B.shapesize(stretch_wid = 5, stretch_len = 0.5)
PADDLE_B.penup()
PADDLE_B.goto(360, 0)

# CODE TO MAKE YOUR BALLS BOUNCE
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("blue")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = 0.3
Ball.dy = -0.3

# I Don't really remember why I named it "pen"
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align = "center",
          font = ("Courier", 25, "normal"))

# Basic functions
# Paddle A
def paddle_a_up():
    y = PADDLE_A.ycor()
    y += 20
    PADDLE_A.sety(y)

def paddle_a_down():
    y = PADDLE_A.ycor()
    y -= 20
    PADDLE_A.sety(y)


# Paddle B
def paddle_b_up():
    y = PADDLE_B.ycor()
    y += 20
    PADDLE_B.sety(y)

def paddle_b_down():
    y = PADDLE_B.ycor()
    y -= 20
    PADDLE_B.sety(y)

# Code to control using the keyboard
SCREEN.listen()
SCREEN.onkeypress(paddle_a_up, "w")
SCREEN.onkeypress(paddle_a_down, "s")
SCREEN.onkeypress(paddle_b_up, "o")
SCREEN.onkeypress(paddle_b_down, "l")

while True:
    SCREEN.update()
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    if Ball.ycor() > 280:
        Ball.sety(280)
        Ball.dy *= -1

    if Ball.ycor() < -280:
        Ball.sety(-280)
        Ball.dy *= -1

    if Ball.xcor() > 380:
        Ball.goto(0, 0)
        Ball.dx *= -1
        SCORE_A += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(SCORE_A, SCORE_B),
                  align="center",
                  font=("Courier", 25, "normal"))

    if Ball.xcor() < - 380:
        Ball.goto(0, 0)
        Ball.dx *= -1
        SCORE_B += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(SCORE_A, SCORE_B),
                  align="center",
                  font=("Courier", 25, "normal"))

    if Ball.xcor() > 340 and (PADDLE_B.ycor() + 50 > Ball.ycor() > PADDLE_B.ycor() - 50):
        Ball.dx *= -1
    if Ball.xcor() < -340 and (PADDLE_A.ycor() + 50 > Ball.ycor() > PADDLE_A.ycor() - 50):
        Ball.dx *= -1



# RUN... RUN... RUN... RUN... RUN...
def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    # Statistics for how good is next generation

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 60)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    run(config_path)
