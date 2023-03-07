weight = float(input("Enter weight in KG")) #Input weight as a float instead of int
height = float(input("Enter height in metres")) #Input height as a float instead of int

BMI = weight/(height*height)

if BMI >= 30:
    print(BMI) #print BMI
    print("User is obese") #print info
if BMI >= 25:
    print(BMI) #print BMI
    print("User is overweight") #print info
if BMI >= 18.5:
    print(BMI) #print BMI
    print("User is normal") #print info
if BMI <= 18.5:
    print(BMI) #print BMI
    print("User is underweight") #print info

    







