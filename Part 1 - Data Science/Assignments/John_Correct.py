name = input("Enter your name: ").lower()

incorrect_names = []

while name != "john":
    incorrect_names.append(name)
    name = input("Enter your name: ").lower()

print(f"Incorrect names: {incorrect_names}")
