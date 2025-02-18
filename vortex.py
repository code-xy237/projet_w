import turtle
colors = ["red", "blue", "green", "gray", "orange", "black"]
a = turtle.Turtle()
a.speed(15)
for i in range(200):
    a.forward(20+i)
    a.left(200 - i/1.5)
    a.color(colors[i%6])
    a.left(50)
    a.forward(133)
