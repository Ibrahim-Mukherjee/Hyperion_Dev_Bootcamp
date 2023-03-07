name1 = input("enter your full age")
parts = name1.split(' ')

if len(parts) == 2:
    print(parts)
    print("the name has two parts")

elif len(parts) != 2:
    print(parts)
    print("the name does not have two parts")

if len(name1) ==0:
    print(parts)
    print("You have not entered anything. Please enter your full name")

if len(name1)<4:
    print(parts)
    print("You have entered less than 4 characters. Please make sure you enter your first name and last name")
    
if len(name1)>25:
    print(parts)
    print("You have entered more than 25 characters. Please make sure you only enter your full name")

elif len(name1) >4 and len(name1) <25:
    print(parts)
    print("Thank you for entering your name")


