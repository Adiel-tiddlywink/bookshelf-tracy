from turtle import *

bgcolor("#e7e9ff")
speed(999)
#title at top
penup()
goto(-290,300)
pendown()
write("Adiel's Showshelf~! (o^▽^o)", font=("Courier", 26, "bold", "italic"))
#top shelf part
penup()
goto(-350, 220)
pendown()
pensize(3)
color("#b9baff")
begin_fill()
circle(25,-180)
right(180)
forward(680)
circle(-25,180)
forward(680)
end_fill()
#middle body
penup()
goto(-320, 220)
pendown()
color("#9c9ee0")
begin_fill()
for i in range(4):
    forward(-600)
    left(-90)
end_fill()
#bottom shelf part
penup()
goto(340, -330)
pendown()
pensize(3)
color("#b9baff")
begin_fill()
circle(25,-180)
right(180)
forward(680)
circle(-25,180)
forward(680)
end_fill()
#dictionary
favShows = {
    "The Owl House":"Dana Terrace",
    "Amphibia":"Matt Braly",
    "K.O.G":"Dana Terrace",
    "Blend S":"Miyuki N.",
    "Glitter Force":"Izumi Todo"
}
#writing out dictionary against the main body
penup()
goto(-290, 300)
pendown()

# x_pos = -300
# y_pos = 100
# line_height = 80

# for key, value in favShows.items():
#     penup()
#     setposition(x_pos, y_pos)
#     write(key, font=("Courier", 20, "bold", "italic"))
#     pendown()
#     y_pos -= line_height

# x_pos = 80
# y_pos = 100
# line_height = 80

# for key, value in favShows.items():
#     penup()
#     setposition(x_pos, y_pos)
#     write(value, font=("Courier", 20, "bold", "italic"))
#     pendown()
#     y_pos -= line_height

# x_pos = -20
# y_pos = 100
# line_height = 80

# for key, value in favShows.items():
#     penup()
#     setposition(x_pos, y_pos)
#     write("by", font=("Courier", 20, "bold", "italic"))
#     pendown()
#     y_pos -= line_height

for index, (name, author) in enumerate(favShows.items()):
    penup()
    sety(150 - (index * 90))
    write(f"{name} by {author}", font=("Courier", 20, "bold", "italic"))
done()