import turtle
import random

ventana = turtle.Screen()
ventana.bgcolor("lightblue")
ventana.title("Corazón")

corazon = turtle.Turtle()
corazon.speed(3)
corazon.color("red")
corazon.begin_fill()

corazon.left(140)
corazon.forward(180)
corazon.circle(-90, 200)
corazon.setheading(60)
corazon.circle(-90, 200)
corazon.forward(180)
corazon.end_fill()

corazon.penup()
corazon.goto(0, -20)
corazon.color("darkred")
corazon.write("Te quiero", align="center", font=("Verdana", 24, "bold"))

def dibujar_mini_figura(t, x, y, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.end_fill()

detalles = turtle.Turtle()
detalles.speed(0)
for _ in range(10):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(["pink", "purple", "yellow", "green"])
    dibujar_mini_figura(detalles, x, y, color)

detalles.hideturtle()

ventana.mainloop()
