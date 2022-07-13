from turtle import *
import turtle as tur

currentshape = "pentagon"

step = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6}

def onkeyshape():
    shape = tur.textinput("Shape Selection", "Enter a shape:")
    if shape.lower() in step:
        tur.reset()
        setcolor(currentcolor)
        setshape(shape.lower())
    tur.listen()  

def setshape(shape):
    global currentshape
    tur.circle(40, None, step[shape])
    currentshape = shape

currentcolor = "purple"

colors = {"pink", "cyan", "light blue", "red", "purple"}

def onkeycolor():
    color = tur.textinput("Color Selection", "Enter a color:")
    if color.lower() in colors:
        tur.reset()
        setcolor(color.lower())
        setshape(currentshape)
    tur.listen()  

def setcolor(color):
    global currentcolor
    tur.color(color)
    currentcolor = color

setcolor(currentcolor)
setshape(currentshape)

tur.onkey(onkeycolor, "c")
tur.onkey(onkeyshape, "s")

tur.listen()

tur.mainloop()