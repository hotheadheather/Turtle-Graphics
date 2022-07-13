from turtle import *

import turtle as tur
from random import randint
 

tur.speed(0)
tur.pensize(10)
tur.colormode(255)
 
while True:
    
    tur.color(randint(0, 255),
          randint(0, 255),
          randint(0, 255))
     

    begin_fill()
     
    tur.circle(20)
     
    end_fill()
     
    tur.penup()
     

    tur.goto(randint(-500, 500), randint(-300, 270))
     

    tur.pendown()