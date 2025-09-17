from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtle_list = []
turtle_positions = [(0,0), (-20,0), (-40,0)]
for position in turtle_positions:
    tim = Turtle(shape="square")
    tim.penup()
    tim.goto(position)
    tim.color("white")
    turtle_list.append(tim)

screen.exitonclick()