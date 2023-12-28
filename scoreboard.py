from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")     # score text color
        self.penup()
        self.goto(0, 270)
        self.hideturtle()       # without adding this method it will show turtle on screen
        self.update_scoreboard()    # calling def update_scoreboard function

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)  # displays score on screen

    def game_over(self):
        self.goto(0,0)  # displays game over in (0,0) position on screen
        self.color("red")
        self.write(arg="GAME OVER", align=ALIGN, font=FONT)  # displays game over on screen


    def increase_score(self):
        self.score += 1     # every time snake hits the food it increase score by 1
        self.clear()        # this clears the previous score
        self.update_scoreboard()    # new score is added on screen