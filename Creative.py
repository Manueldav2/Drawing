import turtle as trtl
import random as rand 
#nike_image = "Nike1.gif"
jordan_image = "jordan1.gif"
wn = trtl.Screen()
wn.title("him")
wn.bgcolor("white")
jermaine = trtl.Turtle()
#wn.addshape(nike_image)
wn.addshape(jordan_image)
#jermaine.shape(nike_image)
jermaine.shape(jordan_image)

question = input("Do you want to walk (Yes or No) ")
title = input("What should the title be? ")
walk = int(input("How many times do you wabt to walk? "))
m = 0
color_list = ["blue","red","green","tan","pink","purple","yellow","brown"]

direction = rand.randint(0,360)
distance = rand.randint(20,50)
color = rand.choice(color_list)
boundary = 100
x,y = jermaine.pos()

wn.title(title)

counter_turtle = trtl.Turtle()
counter_turtle.hideturtle()
counter_turtle.penup()
counter_turtle.goto(-220, 220)
counter_turtle.color("black")
counter_turtle.write("Steps: 0", align="left", font=("Arial", 16, "normal"))
def update_counter():
    counter_turtle.clear()
    counter_turtle.write(f"Steps: {m}", align="left", font=("Arial", 16, "normal"))

if question == "Yes":
    print ("Each step is a diffrent color.")
    for i in range (walk):
        direction = rand.randint(0,360)
        distance = rand.randint(20,50)
        color = rand.choice(color_list)
        boundary = 200
   
        jermaine.setheading(direction)
        jermaine.forward(distance)
        if x > boundary or x < -boundary or y > boundary or y < -boundary:
            jermaine.backward(distance)
        jermaine.pencolor(color)
        m += 1 
        update_counter()

# for i in range (10):
#     jermaine.penup()
#     jermaine.forward(100)
#     jermaine.left(180)
#     jermaine.forward(100)
#     jermaine.left(180)



wn.listen()


wn.mainloop()