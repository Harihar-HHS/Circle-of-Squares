import turtle

def fn():
    obj=turtle.Turtle()
    count = 1
    angle=10
    window=turtle.Screen()
    window.bgcolor("red")
    obj.color("yellow")
    obj.shape("circle")
    obj.speed(10)
    while(count<=36) :            # 360 degrees => 36 rotations of square
        for i in range(0,4):
            obj.forward(50)
            obj.right(90)
        obj.setheading(angle)
        count = count+1
        angle=angle+10
    window.exitonclick()

fn()
