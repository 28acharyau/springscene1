import turtle

screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("deepskyblue2")

t=turtle.Turtle()

t.speed(0)

#water
# t.penup()
# t.goto(-5000,0)
# t.pendown()
# t.fillcolor("steelblue")
# t.pencolor("steelblue")
# t.begin_fill()
# t.goto(5000,0)
# t.goto(5000,-150)
# t.goto(-5000,-150)
# t.goto(-5000,0)
# t.end_fill()


#sand
t.penup()
t.goto(-5000,-50)
t.pendown()
t.fillcolor("forestgreen")
t.pencolor("forestgreen")
t.begin_fill()
t.goto(5000,-100)
t.goto(5000,-5000)
t.goto(-5000,-5000)
t.goto(-5000,-100)
t.end_fill()

#snowman
t.penup()
t.goto(200,-150)
t.pendown()
t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(200,-100)
t.pendown()
t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(200,-70)
t.pendown()
t.fillcolor("white")
t.pencolor("white")
t.begin_fill()
t.circle(15)
t.end_fill()

#sled
t.penup()
t.goto(-200,-200)
t.pendown()
t.pencolor("brown")
t.pensize(10)
t.forward(100)
t.circle(20,180)
t.setheading(0)




t.penup()
t.goto(-100,-100)
t.pendown()
t.fillcolor()
t.pencolor()
t.pensize(20)
t.goto(-100,0)
t.pencolor('green')
t.fillcolor('green')
t.begin_fill()
t.circle(10)
t.end_fill()








turtle.done()
