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

exitonclick()  # Why this? Experiment by commenting it out.