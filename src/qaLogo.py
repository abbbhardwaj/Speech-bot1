import turtle
qas = turtle.Turtle()


def first_turtle():
    qas.pensize(2)
    qas.fillcolor("dark blue")
    qas.begin_fill()
    qas.forward(90)
    qas.left(90)
    qas.forward(12)
    qas.left(90)
    qas.forward(75)
    qas.right(90)
    qas.forward(90)
    qas.left(90)
    qas.forward(13)
    qas.left(90)
    qas.forward(103)
    qas.end_fill()
    qas.penup()


def draw_second():
    qas.goto(80, 20)
    qas.pendown()
    qas.fillcolor("grey")
    qas.begin_fill()
    qas.left(90)
    qas.forward(12)
    qas.left(90)
    qas.forward(80)
    qas.left(90)
    qas.forward(70)
    qas.left(90)
    qas.forward(12)
    qas.left(90)
    qas.forward(58)
    qas.right(90)
    qas.forward(68)
    qas.end_fill()
    qas.penup()


def third_fig():
    qas.goto(42, 51)
    qas.fillcolor("white")
    qas.begin_fill()
    qas.pendown()
    qas.circle(4)
    qas.end_fill()
    qas.penup()


def fourth_fig():
    qas.goto(35, 40)
    qas.pendown()
    qas.fillcolor("grey")
    qas.begin_fill()
    qas.left(90)
    qas.forward(24)
    qas.left(90)
    qas.forward(24)
    qas.left(90)
    qas.forward(24)
    qas.left(90)
    qas.forward(24)
    qas.end_fill()
    qas.penup()


def run_script():
    first_turtle()
    draw_second()
    fourth_fig()
    third_fig()
    turtle.done()


# run_script()