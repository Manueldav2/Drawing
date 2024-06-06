import turtle as trtl
print("\033c")
import random as rand
wn = trtl.Screen()
screen_object = trtl.Screen


# wn.setup(width=1.0, height=1.0)

def changec ():
  random_color = rand.choice(colorlist)
  painter.color(random_color)
  

x1 = 0
y1 = 0

def erase (color): #Erases whats been drawn 
  painter.reset()
  painter.penup()
  painter.goto(0,0)
  painter.color(color)
  painter.pensize(15)
  painter.pendown()

painter = trtl.Turtle()
painter.color("purple")
painter.pensize(15)

#List of  colors 
colorlist = ["blue","red","green","tan","pink","purple","yellow","brown"]
#User input question
question = input("What shall we name this drawing? ")
question2 = input("What should the background color be?...Make sure to spell correctly   ")
colorq = input("What do you want your starting drawing color to be? ")

painter.pencolor(colorq)

colorlist.append(colorq)

print("These are your list of random colors it will change to if you click R.",colorlist,"click C to change color for yourself....")
print("Arrow keys control the direction the turtle draws. The letter   U   puts your pen up and the letter   D   puts pendown. You can draw a semi circle with the key   K  and erase all the drawings with the letter   E  . You can undo what you just drew with the letter “B” and change colors with the letter   C  . You can adjust your turtle in a 45 degree angle instead of 90 in each direction with the use of the key “W” for up and   S   for down . To turn your turtle into an eraser is to use The letter     N  . And last but not least if you click the letter   Z   you're in for a special surprise…")
print('Click screen and use Arrow keys to begin art...')

def semic ():#semi circle
  painter.circle(100,180)


#Initilize screen,u
wn= trtl.Screen()
wn.title(question)
wn.bgcolor(question2)
# for color1 in colorlist:
#   painter.color("color1")
bg_image = "bkinibotom.png"


def squidward():
 squidwardquest = input("What color do you want it? ")
 erase(squidwardquest)
 # wn.bgpic(bg_image)
 questionS = input("Are you sure you want to do this? (Yes or No) ")
 
 if questionS == "Yes":
    questionS2= input("Are you postive?? (Yes or No) ")
 else:
    return

 if questionS2 == "Yes":

  
    painter.penup()
    painter.goto(x1,y1)
    painter.pendown()
    for i in range (4):
      painter.forward(100)
      painter.right(90)
    painter.forward(100)

    painter.forward(100)
    painter.goto(x1,y1)
    painter.forward(200)
    painter.right(90)
    painter.forward(100)
    painter.right(90)
    painter.forward(100)
    painter.left(90)
##Nose
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
    painter.pendown()
    painter.right(90)
    painter.forward(40)
    painter.left(180)
    painter.forward(100)
## Head
    painter.penup()
    painter.forward(150)
    painter.pendown()
    painter.left(90)
    for D in range (4): 
      painter.forward(350) 
      painter.left(90)
    painter.forward(350)
    painter.left(90)
    painter.forward(50)
    painter.forward(200)
    painter.penup()
    painter.forward(100)
    painter.left(90)
    painter.forward(400)
    painter.left(90)
    painter.forward(100)
    painter.pendown()
    painter.forward(100)
    painter.penup()
    painter.forward(100)
    painter.right(90)
    painter.forward(100)
    painter.left(90)
    painter.pendown()
    semic()
    painter.forward(400)
    semic()
    painter.forward(400)
    painter.penup()
    painter.goto(0,0)
    painter.pendown()
    changec
    print ("My squidward is pretty good but try to make something cooler! ")
 else:
    return

distance = 100



def eraser():
  painter.color(colorq)
  painter.pencolor(question2)
  print("Only works with orignal color background...")

def rightlil():
  
  painter.right(45)

def leftlil():
  painter.left(45)



# def forwardlil ():
#   distance = int(input("What distance you want it to move? "))

# distance = 100

# def forward(distance1):
#   distance1 = distance
#   painter.forward(distance1)

def back(): #Back the way you were facing
  painter.left(180)
  painter.forward(100)

def right ():
  painter.right(90)

def left (): #makes turtle turn left
  painter.left(90)

def up ():#Picks pen up so it dosent make unwanted line
  painter.penup()

def down (): #Puts the pen back down aftter it was up 
  painter.pendown()

def semic ():#semi circle
  painter.circle(100,180)


def erase1 (): #Erases whats been drawn 
  painter.reset()
  painter.penup()
  painter.goto(0,0)
  painter.pencolor("purple")
  painter.pensize(15)
  painter.pendown()

def forward():
  painter.forward(100)

# def forwardlil ():
#   distance = int(input("What distance you want it to move? "))

def changecr ():
  random_color = rand.choice(colorlist)
  painter.pencolor(random_color)

def changec ():
  questioncolor = input("What color do you want it? ")
  painter.pencolor(questioncolor)

def backspace():
  painter.undo()

def changebg():
  bgcolor = input("What do you want background color to change too? ")
  wn.bgcolor(bgcolor)


wn.onkeypress(forward, "Up")
wn.onkeypress(back, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")
wn.onkeypress(up, "u")
wn.onkeypress(down, "d")
wn.onkeypress(semic, "k")
wn.onkeypress(erase1, "e")
wn.onkeypress(backspace, "z")
wn.onkeypress(changecr, "r")
wn.onkeypress(rightlil, "s")
wn.onkeypress(leftlil, "w")
wn.onkeypress(squidward, "x")
wn.onkeypress(eraser,"n")
wn.onkeypress(changebg,"b")
wn.onkeypress(changec,"c")
# wn.onkeypress(forwardlil,"f")






wn.listen()


wn.mainloop()





git config --global user.name "Manuel David"
git config --global user.email "Manueldavid500@gmail.com"