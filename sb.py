import turtle
import time

def curvemove_left():
    for i in range(45): #循环200次来绘制一个曲线
        turtle.left(2) #每次循环画笔向右移动1度
        turtle.forward(1) #每次循环画笔向前移动1个单位

def curvemove_right():
    for i in range(45): #循环200次来绘制一个曲线
        turtle.right(2) #每次循环画笔向右移动1度
        turtle.forward(1) #每次循环画笔向前移动1个单位


turtle.color('red')
turtle.left(180)
turtle.forward(140)
curvemove_left()
turtle.forward(120)
curvemove_left()
turtle.forward(120)
curvemove_right()
turtle.forward(120)
curvemove_right()
turtle.forward(140)
turtle.left(180)
turtle.forward(145)

turtle.color('white')
turtle.forward(120)

turtle.color('red')
turtle.left(90)
turtle.forward(355)
turtle.right(90)
turtle.forward(160)
curvemove_right()
turtle.forward(120)
curvemove_right()
turtle.forward(160)
turtle.left(180)
turtle.forward(170)
curvemove_right()
turtle.forward(120)
curvemove_right()
turtle.forward(170)




turtle.done()