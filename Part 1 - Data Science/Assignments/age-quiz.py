#Write a code to input user's age. Store the user's age in an integer variable.
age = int(input("What is your age?"))

if age > 100:
    print("Sorry, you are dead.")

if age > 40:
    print("You're over the hill.")
elif age > 65:
    print("Enjoy your retirement!")

elif age < 13:
    print("You qualify for the kiddie discount.")

elif age == 21:
    print("Congrats on 21!")

else:
    print("Age is but a number.")
