#Conditionals
# Exercise3.1
'''
age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")
'''

#Exercise3.2
'''
score = float(input("Enter score: "))
if score > 90:
    print("A1")
elif score>80:
    print("A2")
elif score>70:
    print("B1")
elif score>60:
    print("B2")
elif score>50:
    print("C1")
elif score>40:
    print("C2")
'''

#Exercise3.3

wheels = int(input("Enter number of wheels: "))

if wheels == 2  :
    print("This is a bicycle")
    battery = input("Enter type of vehicle with battery yes/no")
    if (battery == "yes"):
        print("This E-bike with battery")
    elif battery == "":
        print ("wrong input")
elif wheels ==2 and type == "battery" :
    print("This is a E-bicycle")
elif wheels ==3 :
    print("This is a tricycle")
elif wheels ==4 :
    print("This is a car")
elif wheels > 4 :
    print("This is not such vehicle")

#Exercise 3.4
'''
age = int(input("Enter age: "))
if age>=65:
    print("You are now retired")
elif 18<=age :
    print("Working age")
elif 7<=age<=17:
    print("You are now studying")
elif 0<=age<=6 :
    print("You are a Child")
'''