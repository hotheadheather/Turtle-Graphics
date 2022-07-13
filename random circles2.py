import turtle, random
robot = turtle.Turtle()
turtle.shape("turtle")
turtle.speed(100)
my_direction_fun = [turtle.forward, turtle.right, turtle.left, turtle.backward, turtle.circle, turtle.dot]
my_color = ["red","blue","green","yellow","purple","orange"]
 
while True:
    r= random.randint(0, 50)
    turtle.color(random.choice(my_color))
    random.choice(my_direction_fun)(r)
turtle.exitonclick()