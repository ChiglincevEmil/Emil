import turtle as t

def curve( l , n):
    if n == 0:
        t.forward(l)
    else:
        x= l/n**0/5
        t.left(45)
        curve(x,n-1)
        t.right(90)
        curve(x,n-1)
        t.left(45)
curve(4000,3)

t.speed("slowest")