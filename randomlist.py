import turtle as trtl
import random as rand 
y = 1
z = 1
def checkname():

    while y == 1:
        person = input("What is your name? ")
        if  person in namelist:
            print("in list")
        else:
            print("Not In list")
        checkquest = input("Do you want to check another name? (Yes or No) ")
        if checkquest == ("No"):
            break


def remove():
    while z == 1:
        remove1 = input ("Do you want to remove a person? (Yes or No) ")
        if remove1 == ("No"):
            break
        elif remove1 == ("Yes"):
            removewho = ("What postion is the person you want to remove...starts from 0 ")
            namelist.pop(removewho)



namelist  = ["jhon","thomas","myles"]

add_quest = input("Do you want to add a name? (Yes or No) ") 

x = 1

def addtolist(name):
   namelist.append(name)


if add_quest == ("Yes") :
    while x == 1:
        newname = input("What name do you want to add? ")
        addtolist(newname)
        newname1 = input("Do you want to add another name? (Yes or No) ")
        if newname1 == ("No") :
            break

print("Ok check name.")

checkname()
print(namelist)
remove()

print("end...")