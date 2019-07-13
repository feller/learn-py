from turtle import Turtle, exitonclick
import shapes


def draw_house(tess):
    h = 100
    w = 100
    shapes.draw_rectangle(tess, w, h)
    tess.left(90)
    tess.forward(h)
    tess.right(90)
    shapes.draw_triangle(tess, w)
    tess.right(90)
    tess.forward(h)
    tess.left(90)
    tess.forward(h/3)
    shapes.draw_rectangle(tess, h/3, w/3)


def draw_figures(tess):
    tess.color('red')
    shapes.draw_square(tess, 200)
    tess.color('green')
    shapes.draw_rectangle(tess, 100, 50)
    tess.color('blue')
    shapes.draw_triangle(tess, 70)


def main():
    tess = Turtle()
    tess.shape("turtle")
    draw_house(tess)
    draw_figures(tess)


main()
exitonclick()  # Why this? Experiment by commenting it out.