from turtle import *
import random
import time
import turtle
tur = turtle.Pen()

ws = turtle.Screen()
ws.bgcolor("cyan")
ws.title("Python Guides")

def drawcircle(yellow, blue, red):
	tur.color(yellow, blue, red)
	tur.begin_fill()
	a = random.randint(10,100)
	tur.circle(a) 
	tur.end_fill()
	tur.up() 
	b = random.randint(0,360)
	tur.seth(b)
	# t.acor() is turtle's x; t.ycor() is turtle's y
	if tur.xcor() < -300 or tur.xcor() > 300:
		tur.goto(0, 0)  
	elif tur.ycor() < -300 or tur.ycor() > 300:
		tur.goto(0, 0) 
	c = random.randint(0,100)
	tur.forward(c) 
	tur.down() 

for x in range(0, 100):
	i = random.randint(0,100)/100.0
	j = random.randint(0,100)/100.0
	k = random.randint(0,100)/100.0
	drawcircle(i, j, k)

time.sleep(10)