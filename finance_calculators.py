import math

option = int(input("Enter 1 for investment and 2 for bond calculations"))

if option !=1 or option !=2 :
    print ("You have not selected the right entry, try again")
    option = int(input("Enter 1 for investment and 2 for bond calculations"))

if option == 1:
    money = int(input("Enter the amount of money you are depositing"))
    interest = int(input("Enter the interest rate as a percentage "))
    years = int(input("Enter the amount of time in years you are looking to lend"))
    type = int(input("Enter 1 for simple interest or 2 for compound interest"))
    if type == 1:
        amount = (money * (1+ interest * years))
        print(amount)
        print("this is the amount of money including simple interest")
        
    elif type ==2:
        amount = (money * math.pow(1+interest),years)
        print(amount)
        print("this is the amount accrued including compound interest")

if option ==2 :
    value = int(input("Enter the value of the house"))
    interest = int(input("Enter the interest rate"))
    months = int(input("Enter the total months it would take to repay"))

    repayment = (interest*value)/(1-(1+interest)^(-months))
    print(repayment)
    print("this is the repayment amount to be repaid")



    
    







    







