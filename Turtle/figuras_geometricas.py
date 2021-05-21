import turtle

t = turtle.Turtle()

lado = 3

for i in range(lado):
    t.forward(500/lado)
    t.left(360/lado)

input("")