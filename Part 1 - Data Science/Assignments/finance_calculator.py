import math

#The User will be able to choose which calculation they want to do. Ask the user to input option. 
#All Lower Case Input!
invest_choice = "investment"
bond_choice = "bond"

interest_choice = input("If you want to calculate the amount of interest you'll earn on your investment, type 'investment'. If you want to calculate how much money you will repay on a bond, type 'bond'. ").lower()

#If the User selects "investment," set up the formula by collecting the information.
if interest_choice == invest_choice:

    #Collect information for the variables in the mathmatic equations.
    #Have User input in all lower.
    inital_deposit = int(input("How much money are you depositing?"))
    annual_interest = int(input("Please enter your annual interest rate in percentage form. For example, 8 percent is typed as 8."))
    interest_rate = annual_interest / 100 
    years = int(input("Enter the number of years the money is being invested."))

    #Ask the User to input which interest formula they wish to calculate.
    #Make variables with the word value User is inputting.
    simple_interest = "simple"
    comp_interest = "compound"

    #Have the User choose which variable's word value to type.
    user_interest = input("Type 'simple' if you want to calculate your simple interest, or 'compound' if you want to calculate your compound interest.").lower()
    
    #If user types "simple"
    if user_interest== simple_interest:
        simple_calculation = float(inital_deposit * (1 + interest_rate*years))
        
        #Get Output in Sentence
        sentence_simple = f"Your simple interest is ${simple_calculation}"
        print(sentence_simple)
    
    #If user types "compound"
    elif user_interest == comp_interest:
        compound_calculation = float(inital_deposit * math.pow((1+interest_rate),years))
        
        #Get the Output in Sentence
        sentence_compound = f"Your compound interest is ${compound_calculation}"
        print(sentence_compound)
    

#Now we are calculating the bond value. Check the indentation and formatting.
elif interest_choice == bond_choice:
    
    #We are going to collect the data for this equation. This equation is different.
    home_value = int(input("Enter the present value of your home."))
    monthly_interest = int(input("Please enter your monthly interest rate in percentage form. For example, 8 percent is 8. "))
    monthly_rate = monthly_interest / 100 / 12
    months = int(input("Please enter the number of months you will be repaying your bond."))

    bond_pay= (monthly_rate*home_value) / (1-(1+monthly_rate)**(-months))

    #Output the Answer
    sentence_bond = f"Every month you will pay ${bond_pay}."
    print(sentence_bond)
