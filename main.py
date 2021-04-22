import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(200):
    degree = [0, 90, 180, 270]
    direction = random.choice(degree) 
    tim.setheading(direction)
    tim.color(random.choice(colours))
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(20)