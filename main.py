import turtle
import random
from turtle import Turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle")

score_turtle = turtle.Turtle()

FONT = ("Arial",30,"normal")
score=0
game_over=False

countdown_turtle: Turtle=turtle.Turtle()


turtle_list=[]

def setup_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height=drawing_board.window_height()
    y = top_height*0.49


    score_turtle.setpos(0,y)
    score_turtle.write("Score: 0", move=False,align="center", font=FONT)
    score_turtle.hideturtle()

grid_size=10
def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)


x_coordinates=[-20,-10,0,10,20]
y_coordinates=[-20,-10,0,10,20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        drawing_board.ontimer(show_turtle_randomly, 500)

def countdown(time):
    global game_over
    countdown_turtle.color("dark blue")
    countdown_turtle.penup()

    top_height = drawing_board.window_height()
    y = top_height * 0.35

    countdown_turtle.setpos(0, y)

    if time>0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time),move=False, align="Center",font=FONT)
        drawing_board.ontimer(lambda: countdown(time-1),1000)
    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!".format(time), move=False, align="Center", font=FONT)


    countdown_turtle.hideturtle()


turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtle_randomly()
countdown(15)
turtle.tracer(1)
turtle.mainloop()


