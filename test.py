from turtle import Turtle, Screen

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.color("white")
tim.write("Hello World", True, align = "center", font=('Arial', 25, 'normal'))
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('grey')
screen.title("Snake Game")



screen.exitonclick()