from turtle import *

width(7)
color("brown")

begin_fill()

forward(200)
left(90)
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)

end_fill()


color("gold")
penup()
goto(70, 0)
begin_fill()
left(90)
forward(120)    
right(90)

forward(60)
right(90)
forward(120)

end_fill()

penup()
goto(200, 200)
pendown()

color("maroon")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#Drawing window
penup()
goto(20, 170)
pendown()

color("aqua")
begin_fill()
left(120)
forward(160)
right(90)
forward(40)
right(90)
forward(160)
right(90)
forward(40)
end_fill()

#Draw door lock
penup()
goto(110, 50)
pendown()

color("yellow")
right(90)
forward(10)
exitonclick()