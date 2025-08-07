#I am using the for_example2 file as my base for this assignment.

given_number = int(input("Enter a number: \n"))

#Combining a for-loop with an If Statement
if given_number % 2 == 0:  # If number is even.
    stars = "**"
    for i in range(1, 5):
        print(stars)
        stars = stars + "**"

elif (given_number % 2 != 0):  # If number is odd, i.e. the number divided by 2 does NOT have a remainder of 0.
    stars = "**********"
    for i in range(1, 5):
        index = 10 - i * 2
        print(stars[0:index])

#Reverse the code to get the otherside of the arrow.
reversed_number = int(input("Enter an odd number: \n"))

if reversed_number % 2 == 0:
    stars = "**"
    for i in range(1, 5):
        print(stars)
        stars = stars + "**"
elif reversed_number % 2 != 0:
    stars = "**********"
    for i in range(1, 5):
        index = 10 - i * 2
        print(stars[0:index])

#Join the two loops to create full arrow figure.