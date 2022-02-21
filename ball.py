from turtle import Turtle


class Ball:
    def __init__(self):
        super().__init__()
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.turtlesize(2, 2)
        self.ball.color("white")
        self.ball.penup()

    def first_move(self):
            new_x = self.ball.xcor() + 1
            new_y = self.ball.ycor() + 1
            self.ball.setpos(new_x,new_y)

