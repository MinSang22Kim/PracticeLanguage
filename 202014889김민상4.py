import turtle as t
import random

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('white')

balls = []

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']

class Ball:
    def __init__(self, size):
        self.size = size
        self.color = random.choice(colors)
        self.speed = random.uniform(1, 9)
        self.direction = random.randint(0, 360)
        self.x = 0  # 가운데에서 시작
        self.y = 0  # 가운데에서 시작

        self.turtle = t.Turtle()
        self.turtle.shape('circle')
        self.turtle.color(self.color)
        self.turtle.shapesize(self.size)
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)

    def move(self):
        self.turtle.setheading(self.direction)
        self.turtle.forward(self.speed)

        if self.turtle.xcor() > screen.window_width() // 2 - 10 or self.turtle.xcor() < -screen.window_width() // 2 + 10:
            self.direction = 180 - self.direction

        if self.turtle.ycor() > screen.window_height() // 2 - 10 or self.turtle.ycor() < -screen.window_height() // 2 + 10:
            self.direction = -self.direction

for _ in range(20):
    size = random.uniform(0.5, 7)
    ball = Ball(size)
    balls.append(ball)

screen.tracer(0)

while True:
    for ball in balls:
        ball.move()

    screen.update()

t.done()
