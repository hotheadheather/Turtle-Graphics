def star (t,sides,length):
    for x in range(sides):
        t.forward(length)
        t.right(180-180/sides)

def polygon(t,sides,length):
    t.forward(length)
    t.left(360/sides)