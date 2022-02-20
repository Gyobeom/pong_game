from turtle import Turtle
block_position = [(350,100),(350,80),(350,60),(350,40),(350,20),(350,0)]




class Paddle:
    def __init__(self):
        self.all_block = []
        self.create_block()

    def create_block(self):
        for block_index in block_position:
            block = Turtle()
            block.hideturtle()
            block.shape("square")
            block.hideturtle()
            block.color("white")
            block.turtlesize(1.5)
            block.penup()
            block.goto(block_index)
            self.all_block.append(block)
        for block_index in self.all_block:
            block_index.showturtle()


    # def showe_block(self):
    #     for block_index in self.all_block:


    # def right_paddle(self):
    #     self.hideturtle()
    #     self.penup()
    #     self.shape("square")
    #     self.color("white")
    #     self.turtlesize(10,2)
    #     self.goto(x=350, y=0)
    #     self.showturtle()
    #
    # def up_paddle(self):
    #     self.forward(20)
