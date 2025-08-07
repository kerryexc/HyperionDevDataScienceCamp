#Ask the user to input three numbers. Turn answer into integer.
Num1 = int(input("Enter a number."))
Num2 = int(input("Enter a number"))
Num3 = int(input("Enter a number."))

#Calculate the sum of integers. Combine variables
numbers_list = [Num1,Num2,Num3]
x_sum = print(sum(numbers_list))

#Calculate the first number minus the second number.
print(Num1 - Num3)

#Calculate the third number multiplied by the first number.
print(Num3*Num1)

#Calculate the sum of all three numbers divided by the third number.
print(sum(numbers_list)/Num3)