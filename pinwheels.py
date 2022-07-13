from turtle import *
from random import randint

speed(0)
pensize(4)
colormode(255)

for i in range(30):
  color(randint(50,150),randint(50,150),randint(50,150))
  for i in range(24):
    forward(50)
    left(90)
    forward(50) 
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    left(15)
  penup()
  goto(randint(-500,500), (-300,270))
  pendown()
  done()
  