import math
menu = print("Welcome, \n Choose either 'investment' or 'bond' from the menu below to proceed: \n investment - to calculate the amount of interest you'll earn on interest. \n bond - to calculate the amount you'll have to pay on a home loan.")
selection = input("Enter your selection:").lower()
future = "investment"
monthly = "bond"
simple = "simple" 
compound = "compound"
interest = "interest"
#bond option            
if selection == monthly:
        house = float(input("What is the present value of the house?:"))
        rate_int2 = float(input("Enter interest rate:"))
        repay_ = int(input("Enter the amounts of months to repay the bond:"))
        monthly_interest = house * (rate_int2 / 100 / 12)
        number_months = math.pow((1 + rate_int2 / 12 / 100),-repay_)
        repayment = monthly_interest / (1 - number_months)
        print("The amount you will pay for the bond each month is R", repayment)
#investment option
if selection == future:
    principal = int(input("Enter the amount of money to deposit:"))
    rate_int1 = float(input("Enter the interest rate:"))
    time = int(input("Enter the amount of years you plan to invest:"))
    interest = input("Do you want simple or compound interest for your investment?:")
#investment type
if interest == simple:
        total_amount = principal * (rate_int1 / 100) * time + principal
        print(f"You will receive R {total_amount} at the end of your investment period")
elif interest == compound:
        total_amount2 = principal * math.pow((1 + rate_int1 / 100),time)
        print(f"You will receive R{total_amount2} at the end of your invest period")
#invalid error text              
else:
        print("Invalid choice. Choose either 'investment' or 'bond'.")
       

 



    
