__author__ = 'student'
import turtle

def curve( l , n):
    if n == 0:
        turtle.forward(l)
    else:
        x= l/4
        curve(x, n-1)
        turtle.left(60)
        curve(x, n-1)
        turtle.right(120)
        curve(x , n-1)
        turtle.left(60)
        curve(x, n-1)
turtle.speed('slowest')
curve(40000, 5)