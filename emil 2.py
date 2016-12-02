import turtle as t

def curve( l , n, an=45):
    if n == 0:
        t.forward(l)
    else:
        x= l/1.6
        t.left(an)
        curve(x,n-1, 45)
        t.right(an*2)
        curve(x,n-1, -45)
        t.left(an)


curve(400000,20)

t.speed("slowest")