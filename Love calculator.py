#Firstly i add the random function to help with the more detail part of the maths.
import random
print("Welcome to the DSC love calculator")

#Then take the 2 names as inputs.
name_one = input("What is your name?: ")
name_two = input("What is their name?: ")

#Then turn them into lower case.
"name_one".lower()
"name_two".lower()

#And count the number of characters each name has.
boy = len(name_one)
girl = len(name_two)

#Then here the random.randint function takes a while guess between 1 and 20 to give a decimal number.
rnd = random.randint(1,20)

#Now here i subtract boy's total multiplied by girl's total from hundred% and then the random.randint from hundred%
percentage = 100 - (boy*girl) - rnd

#Now here using str percentage is changed to digit form and and the end a "%" .
print("Chances of true love together is " + str(percentage)+"%")
