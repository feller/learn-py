from turtle import Turtle, exitonclick
import shapes

tess = Turtle()
tess.shape("turtle")

tess.color('red')
shapes.draw_square(tess, 100)
tess.color('green')
shapes.draw_rectangle(tess, 50, 20)

exitonclick()  # Why this? Experiment by commenting it out.