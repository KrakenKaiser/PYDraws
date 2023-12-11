import turtle

def draw_petal(t, radius, angle):
    t.begin_fill()
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)
    t.end_fill()

screen = turtle.Screen()
screen.bgcolor("blue")

sunflower = turtle.Turtle()
sunflower.speed(10)

sunflower.color("yellow")
for _ in range(12):
    draw_petal(sunflower, 100, 60)
    sunflower.left(30)

sunflower.penup()
sunflower.goto(0, -20)
sunflower.pendown()

sunflower.color("brown")
sunflower.begin_fill()
sunflower.circle(20)
sunflower.end_fill()

sunflower.hideturtle()
screen.mainloop()
