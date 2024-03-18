from turtle import Turtle
import math
t = Turtle()
centerPoint = (0.0, 0.0)
circleRadius = int(input("Please enter the radius of the circle: "))
forward = int(input("Please enter how far the turtle should moved: "))

def drawCircle(t, centerPoint, circleRadius, forward):
    t.goto(centerPoint)
    t.setheading(3)
    t.forward(forward * 120)
    t.circle(circleRadius)

drawCircle(t, centerPoint, forward, circleRadius)
distanceMoved = 2.0 * math.pi * circleRadius / 120.0
print("Distance moved is...", distanceMoved)
input("Press enter to close...")
