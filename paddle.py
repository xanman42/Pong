from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, xcord):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.setx(xcord)

    def up(self):
        self.sety(self.ycor()+35)

    def down(self):
        self.sety(self.ycor()-35)
