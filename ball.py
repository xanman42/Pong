from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(50)
        self.y_direction = +10
        self.x_direction = +10

    def move(self):

        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def wallcollider(self):
        if self.ycor() < -285 or self.ycor() > 285:
            self.bounce('W')

    def bounce(self, W_or_P):
        if W_or_P == 'W':
            self.y_direction = - self.y_direction

        # self.setheading(90)

    def reset_position(self):
        self.goto(0, 0)
        if self.y_direction > 0:
            self.y_direction += 1
        else:
            self.y_direction -= 1
        if self.x_direction > 0:
            self.x_direction += 1
        else:
            self.x_direction -= 1
