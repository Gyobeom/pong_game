from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)


    def up_paddle(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.setpos(new_x,new_y)


    def down_paddle(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.setpos(new_x,new_y)

    def l_up_paddle(self):
        new_x = self.xcor()
        new_y = self.ycor() + 20
        self.setpos(new_x,new_y)


    def l_down_paddle(self):
        new_x = self.xcor()
        new_y = self.ycor() - 20
        self.setpos(new_x,new_y)

