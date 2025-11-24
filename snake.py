from turtle import Turtle

def create_turtle():
    t = Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    return t

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []

        x_cord = 0
        for _ in range(3):
            t = create_turtle()
            self.segments.append(t)
            t.setx(x_cord)
            x_cord -= 20
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x =  self.segments[seg_num - 1].xcor()
            new_y =  self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].seth(RIGHT)

