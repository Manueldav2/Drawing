''''
import turtle as trtl



painter = trtl.Turtle()



color2 = input("what color shape do you want? ")
painter.pencolor(color2)
x1= int(input("what x value do you want? ")) ## cast intput to integer by double parenthese and put int
y2= int (input("what y value do you want? "))
##Face
painter.penup()
painter.goto(x1,y2)
painter.pendown()
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.goto(x1,y2)
painter.forward(200)
painter.right(90)
painter.forward(100)
painter.right(90)
painter.forward(100)
painter.left(90)
##Nose
painter.pencolor("lightblue")
painter.pensize(15)
painter.forward(150)
painter.right(90)
painter.forward(35)
painter.right(90)
painter.forward(150)
painter.right(180)
painter.forward(150)
painter.penup()
painter.forward(30)
## Smile
painter.color("gold")
painter.pendown()
painter.right(90)
painter.forward(40)
painter.left(180)
painter.forward(100)
## Head
painter.color("lavender")
painter.penup()
painter.forward(150)
painter.pendown()
painter.left(90)
painter.forward(350)
painter.left(90)
painter.forward(350)
painter.left(90)
painter.forward(400)
painter.left(90)
painter.forward(350)
painter.left(90)
painter.forward(50)
wn = trtl.Screen()

wn.mainloop()
'''
import turtle as trtl
wn = trtl.Screen()
 
my_turtles = [] # Create an empty list

# Shapes and colors list
turtle_shapes = ["arrow","turtle","circle","square","triangle","classic"]
turtle_colors = ["black","blue","purple","gold","skyblue","lightcoral"]

# Add shapes and colors to my_turtles list

for shape_getter in turtle_shapes: # this loop set each of the variables
  traffic_turtle = trtl.Turtle(shape_getter) # sets the turtle to the nest shape in the list
  new_color = turtle_colors.pop() # Removes the last element anad assigns it to a variable
  traffic_turtle.color(new_color) # Sets the turtle color to the color that was just popped
  my_turtles.append(traffic_turtle) # append shapes in list order

x_loc = 0 # Set x location of turtle
y_loc = 0 # Set y location of turtle
direction = -45 # set the start direction
traffic_turtle.goto(x_loc,y_loc) # turtle goes to the start coordinates determined on lines 20 & 21
distance = 20 # sets the length of the lines to 10

turtle_location = traffic_turtle.pos() # puts the location of the turtle into a variable
traffic_turtle.speed(0) # Makes the turtle speed the fastest

for traffic_turtle in my_turtles*3: # repeats the loop the amount three times of items in the my_turtles variable
  traffic_turtle.penup() # picks pen up
  traffic_turtle.goto(turtle_location) # goes to the location where the turtles most recently stopped
  traffic_turtle.pendown() # puts pen down
  traffic_turtle.setheading(direction) # points in the direction of the direction variable
  traffic_turtle.forward(distance) # turtle moves the distance of the distance variable
  direction -= 45 # Changes the direction by 45 degrees
  turtle_location = traffic_turtle.pos() # puts the location of the turtle into a variable
  distance += 10 # the distance goes up by 10
  traffic_turtle.stamp() # stamps turtle

wn.mainloop() # This keeps the screen on