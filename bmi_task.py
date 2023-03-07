weight = int(input("Enter weight in KG"))
height = int(input("Enter height in metres"))

BMI = weight/(height*height)

if BMI >= 30:
    print("User is obese")
if BMI >= 25:
    print("User is overweight")
if BMI >= 18.5:
    print("User is normal")
if BMI <= 18.5:
    print("User is underweight")

    







