from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Paddle(Turtle):
    def __init__(self, pos):
        position = pos
        super().__init__()
        self.block = Turtle()
        self.block.hideturtle()
        self.block.penup()
        self.block.shape("square")
        self.block.color("white")
        self.block.setheading(UP)
        self.block.turtlesize(2, 10)
        self.block.setpos(position)
        self.block.showturtle()


    def up_paddle(self):
        new_x = self.block.xcor()
        new_y = self.block.ycor() + 20
        self.block.setpos(new_x,new_y)


    def down_paddle(self):
        new_x = self.block.xcor()
        new_y = self.block.ycor() - 20
        self.block.setpos(new_x,new_y)

    def l_up_paddle(self):
        new_x = self.block.xcor()
        new_y = self.block.ycor() + 20
        self.block.setpos(new_x,new_y)


    def l_down_paddle(self):
        new_x = self.block.xcor()
        new_y = self.block.ycor() - 20
        self.block.setpos(new_x,new_y)

