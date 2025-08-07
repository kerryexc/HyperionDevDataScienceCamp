#Ask user to input name. 

names = []

while True:
    name = input("Enter a name: ").lower()
    if name.lower() == "john":  # Use .lower() for case-insensitive check
        break
    if name != "john":  # Check if the name is NOT John before appending
        names.append(name)

print("Names entered:", names)
