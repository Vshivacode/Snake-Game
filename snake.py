from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]    # assigning the segments[0] = head of snake

    def create_snake(self):
        for position in STARTING_POSITIONS:     # this position item is used as x,y cordinates in goto(position)
            self.add_segment(position)  # calling add_segment function

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()  # clear the lines drawn by turtle
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_length(self):    # here position = (-40,0) so it add one segment to this position
        self.add_segment(self.segments[-1].position())  # adding one segment to end of the tail that is segments[-1]

    def move(self):
        for last_part in range(len(self.segments) - 1, 0, -1):  # start = len(segments), stop = 0 and step = -1
            new_x = self.segments[last_part - 1].xcor()  # second body part is moved to first body part
            new_y = self.segments[last_part - 1].ycor()
            self.segments[last_part].goto(new_x, new_y)  # tale of snake moved to second last position of body
        self.head.forward(MOVE_DISTANCE)  # finally the 3 body parts are linked and moving at single time

    def up(self):
        if self.head.heading() != DOWN:      # .heading is used to tell direction of head of the snake
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
