import turtle

STARTING_POINTS: list = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        # TODO:1 -Create a snake body.
        self.segments = []
        self.create_snake()
        # loop through the starting positions to create three turtle objects

    def create_snake(self):
        for position in STARTING_POINTS:
            self.add_new_segment(position)

    def add_new_segment(self, position):
        snake = turtle.Turtle("square")
        snake.color("white")
        # This way each snake won't draw the lines as they move from one position to the next
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_new_segment(self.segments[-1].position())

    def move(self):

        for element in range(len(self.segments) - 1, 0, -1):
            # Get hold of the position of the second last element
            new_x = self.segments[element - 1].xcor()
            new_y = self.segments[element - 1].ycor()
            # Now tell the last element to move to the position of the second last element
            self.segments[element].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)



