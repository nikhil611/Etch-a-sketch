from turtle import Turtle, Screen

tim = Turtle()
Screen = Screen()


def move_forwards():
    tim.forward(10)
def move_forward():
    tim.forward(10)
def move_backword():
    tim.backward(10)
def move_left():
    new_heading = tim.left(45)
    tim.setheading(new_heading)
def move_right():
    new_heading = tim.right(45)
    tim.setheading(new_heading)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


Screen.listen()
Screen.onkey(move_forward , "w")
Screen.onkey(move_backword, 's')
Screen.onkey(move_left , 'a')
Screen.onkey(move_right , 'd')
Screen.onkey(clear , "c")
Screen.exitonclick()
