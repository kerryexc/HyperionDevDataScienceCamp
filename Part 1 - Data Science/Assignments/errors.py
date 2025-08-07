# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #No parentheses to close the string.

# Variables declaring the user's age, casting the str to an int, and printing the result
user_age = 24 #make this a variable. 
print(f"I'm {user_age} years old.") #must prefix string with f and use curly braces to input user_age into sentence.

# Variables declaring additional years and printing the total years of age
years = 3
total_years = user_age + years #make an addition equation
print(total_years) #get answer to user age and the other year added on. This prints the output of the equation

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12 #make sure right variable is being used in equation
print(f"In 3 years and 6 months, I will be {total_months + 6 } months old.") #follows same format as the first print request on line 10. However, we are adding 6 months to this.

#HINT, 330 months is the correct answer

