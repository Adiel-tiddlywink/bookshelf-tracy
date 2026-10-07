from turtle import *

shape("turtle")
bgcolor("#c0f5f7")
pensize(5)

print(pos())

#square
# for i in range(4):
#     forward(50) #pixels
#     left(90)

penup()
goto(-160, 250)
pendown()
write("Squirtle's Pokeball!", font=("Courier", 26, "bold"))

penup()
goto(0,0)
pendown()
# right(90)
# circle(100, 180) #radius,degrees

#top half
left(90)
color("red")
begin_fill()
circle(50,180)
end_fill()

#bottom half
color("black")
begin_fill()
color("white")
circle(50,180)
end_fill()

#middle line
color("black")
pensize(3)
left(90)
forward(100)

#innermost black circle
left(180)
forward(30)
right(90)
begin_fill()
circle(20)
end_fill()

#innermost white circle
left(90)
forward(5)
right(90)
color("white")
begin_fill()
circle(15)
end_fill()

#innermost black circle
width(1)
color("black")
penup()
left(90)
forward(3)
right(90)
pendown()
circle(12)

hideturtle()
#keeps window open
done()