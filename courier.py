price = int(input("Enter price of the packet"))
kilometres = int(input("Enter the distance to send in Kilometres"))
select = int(input("Enter 1 for air or enter 2 with freight"))
select2 = int(input("Enter 1 for full insurance or 2 for partial insurance"))
select3 = int(input("Enter 1 for Gift or 2 for no gift"))
select4 = int(input("Enter 1 for priority or 2 for not priority"))


cost_per_distance = 0
if select ==1 :
    cost_per_distance = 0.25
elif select ==2 :
    cost_per_distance = 0.36

insurance_cost = 0
if select2 ==1 :
    insurance_cost = 50
elif select2 ==2:
    insurance_cost = 25

gift_cost = 0
if select3 ==1 :
    gift_cost = 15
elif select3 ==2 :
    gift_cost = 0

priority_or_standard_delivery = 0
if select4 ==1 :
    priority_or_standard_delivery = 100

elif select4 == 2:
    priority_or_standard_delivery = 20


total_cost = price + kilometres*cost_per_distance + insurance_cost + gift_cost + priority_or_standard_delivery
print (f"""\nThis is your Total cost:
${total_cost}""")




