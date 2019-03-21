from turtle import Turtle, exitonclick
import shapes

tess = Turtle()
tess.shape("turtle")

tess.color('red')
shapes.draw_square(tess, 200)
tess.color('green')
shapes.draw_rectangle(tess, 100, 50)
tess.color('blue')
shapes.draw_triangle(tess, 70)

for i in range(3):
    tess.left(20)
    shapes.draw_square(tess, 90)

tess.left(180)
tess.forward(200)
shapes.draw_rectangle(tess, 100, 50)
shapes.draw_triangle(tess, 70)


exitonclick()  # Why this? Experiment by commenting it out.