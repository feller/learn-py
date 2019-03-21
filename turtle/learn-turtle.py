from turtle import Turtle, exitonclick
import shapes

tess = Turtle()
tess.shape("turtle")


shapes.draw_square(tess)

exitonclick()  # Why this? Experiment by commenting it out.