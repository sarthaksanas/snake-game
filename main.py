from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

turtle_list = []
turtle_positions = [(0,0), (-20,0), (-40,0)]
for position in turtle_positions:
    tim = Turtle(shape="square")
    tim.penup()
    tim.goto(position)
    tim.color("white")
    turtle_list.append(tim)

game_on = 20

while game_on > 0:
    screen.update()
    time.sleep(0.1)
    for turtle_num in range(len(turtle_list) - 1, 0, -1):
        new_x = turtle_list[turtle_num - 1].xcor()
        new_y = turtle_list[turtle_num - 1].ycor()
        turtle_list[turtle_num].goto(new_x, new_y)
    turtle_list[0].forward(20)
    game_on -= 1

screen.exitonclick()
