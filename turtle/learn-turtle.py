from turtle import Turtle, exitonclick
import shapes

tess = Turtle()
tess.shape("turtle")

shapes.draw_square(tess, 50)

exitonclick()  # Why this? Experiment by commenting it out.