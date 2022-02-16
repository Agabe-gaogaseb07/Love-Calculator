import random
print("Welcome to the DSC love calculator")

name_one = input("What is your name?: ")
name_two = input("What is their name?: ")
"name_one".lower()
"name_two".lower()
boy = len(name_one)
girl = len(name_two)
rnd = random.randint(1,20)
percentage = 100 - (boy*girl) - rnd

print("Chances of true love together is " + str(percentage)+"%")