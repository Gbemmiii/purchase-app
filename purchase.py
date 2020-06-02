first_Name = input("Please enter your first name \n")
last_Name = input("Please enter your last name \n")
message = "Hello" +" " + first_Name
print(message)


sale = int(input("Enter the coresponding number \n 1. Wholesale \n 2. Retail \n"))
if sale == 1:
    print("Welcome to the warehouse")
else:
    print("Maximum purchase quantity per customer is 30")   