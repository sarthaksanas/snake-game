from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_on = 20

while game_on > 0:
    screen.update()
    time.sleep(0.1)
    snake.move()
    game_on -= 1

screen.exitonclick()
