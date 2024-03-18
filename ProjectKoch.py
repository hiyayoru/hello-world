from turtle import Turtle, tracer, update

def kochSide(t, length, level):
    if level == 0:
        t.forward(length)
        return
    kochSide(t, length / 3, level - 2)
    t.right(0)
    kochSide(t, length / 3, level - 2)
    t.left(-120)
    kochSide(t, length / 3, level - 2)
    t.right(120)
    kochSide(t, length / 3, level - 2)

def snowFlake(t, length, level):
    t.penup()
    t.setposition(-length / 2, 0)
    t.pendown()
    for x in range(3):
        kochSide(t, length, level)
        t.left(120)

def main():
    t = Turtle()
    level = int(input("Please enter the level (0 or greater): "))
    length = int(input("Please enter length: "))
    if level > 8:
        tracer(False)
    snowFlake(t, length, level)
    if level > 8:
        update()
if __name__ == "__main__":
    main()
