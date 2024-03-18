from turtle import Turtle, tracer, update, Screen 
import random

def cCurve(t, level, x1, y1, x2, y2):

    def drawLine(x1, y1, x2, y2):
        t.pencolor(random.randint(0, 255), # This changes the pencolor every time it draws a line which allows us to create a cCurve that will change colors as its drawn
                random.randint(0, 255),
                random.randint(0, 255))
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
        

    if level == 0:
        drawLine(x1, y1, x2, y2) # States that if level is 0 then it only draws one line

    else:
        xm = (x1 + x2 + y1 - y2) / 2 # States that if level is more than 0 then it draws more than 1 line
        ym = (x2 + y1 + y2 - x1) / 2
        cCurve(t, level - 1, x1, y1, xm, ym)
        cCurve(t, level - 1, xm, ym, x2, y2)

def main(): # main function that asks for the user to input the level and then calls the cCurve function
    level = int(input("Enter the level (0 or greater): "))
    t = Turtle()
    screen = Screen() 
    screen.colormode(255) # added screen purely because without this then t.pencolor()wouldn't accept colors from 0 to 255
    if level > 8:
        tracer(False)
    t.hideturtle()
    cCurve(t, level, 50, -50, 50, 50)
    if level > 8:
        update()


if __name__ == "__main__":
    main()
