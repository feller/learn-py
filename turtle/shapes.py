def draw_square(turtle, length=100):
    draw_rectangle(turtle, length, length)


def draw_rectangle(turtle, width=100, height=50):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


def draw_triangle(turtle, length=100):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


