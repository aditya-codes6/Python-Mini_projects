## inputs that we need to make this calculator
# Total amount of rent 
# Total food/snack amount
# Electricity bill 
# Charge per unit 
# Total amount you have to pay
# Total person who shares the bill

#                    START                      #
 
rent = int(input("Enter the total rent = "))
food = int(input("Enter the total food spendings = "))
electricity = int(input("Enter the electricity unit ="))
unit = int(input("Enter the charge per unit = "))
person =  int(input("Enter the person who shares the amount"))

x = electricity * unit
output = (food + rent + x)//person
print("output =" , output)