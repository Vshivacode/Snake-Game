from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

my_screen = Screen()
my_screen.setup(width = 600, height = 600)
my_screen.bgcolor("black")              # changes the background color to black
my_screen.title("My Snake Game")        # shows title on popup window in border not inside the screen
my_screen.tracer(0)                     # it is used to off the animation


snake = Snake()
food = Food()
scoreboard = Scoreboard()


my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    my_screen.update()                                  # it is used to update the animation on
    time.sleep(0.1)                                     # speed of the snake
    snake.move()

    # Detect Collision with Food using distance() method
    if snake.head.distance(food) < 15:      # 15 is the size of the food radius
        food.refresh()
        snake.extend_length()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()


    # Detect collision with tail
    # if snake head collides with his own tail then return GAME OVER
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

my_screen.exitonclick()