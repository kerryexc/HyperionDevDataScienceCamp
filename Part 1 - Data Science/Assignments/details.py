# collecting the name, age, street number, and street name. You must ask the user to input these.
name_er = input("What is your name?")
age_er = float(input("How old are you?"))
house_er = int(input("What is your street number?"))
street_name = input("What is the name of your street?")

# f string includes variables into the string. You must use the curley brackets!
print(f"My name is {name_er} and I am {age_er} years old. I live on {house_er}{street_name}.")
