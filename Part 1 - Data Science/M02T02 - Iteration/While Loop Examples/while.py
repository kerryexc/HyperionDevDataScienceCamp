#Write a program that continually asks the user to enter a number. 
#When the user enters "-1" the program should stop requesting the user enters a number.
#Calculate the average of the valid numbers entered, excluding -1 and 0.
#Use a WHILE LOOP to achieve this.


#Ask user to input a number.
#Make the user inputs into a list.
input_list = []
user_input = int(input("Enter a number from -1 to 100, excluding 0."))

#Loop until user enters -1
while user_input> -1:
    user_input = int(input("Enter a number from -1 to 100, excluding 0."))
    input_list.append(user_input)

    #This is a form of breaking the loop with a break statement;
    # Does -1 count as part of the average?
    if user_input == -1:
        break
    
print(input_list)

#Is there a way to make a range in a calculation that excludes the number 0?
average = sum(input_list) / len(input_list)
print(average)








