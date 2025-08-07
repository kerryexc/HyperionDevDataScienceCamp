# Create a class for the shoes
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)
    
    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"Country: {self.country}, Code: {self.code}, "
                f"Product: {self.product}, Cost: ${self.cost:.2f}, "
                f"Quantity: {self.quantity}")

#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============

# Create the functions for each task of the inventory
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip header line
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    # To deal with value errors etc...
    except FileNotFoundError:
        print("File not found. Please ensure 'inventory.txt' exists.")
    except ValueError as e:
        print(f"Error processing line: {line.strip()} -> {e}")

def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter shoe code: ")
    product = input("Enter product name: ")
    try:
        cost = float(input("Enter cost: "))
        quantity = int(input("Enter quantity: "))
        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)
        print("Shoe added successfully!")
    except ValueError:
        print("Invalid cost or quantity. Please enter numeric values.")

def view_all():
    if not shoe_list:
        print("No shoes in the list.")
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    if not shoe_list:
        print("Shoe list is empty.")
        return

    lowest = min(shoe_list, key=lambda x: x.get_quantity())
    print(f"Lowest stock item:\n{lowest}")
    try:
        add_qty = int(input("Enter quantity to add: "))
        lowest.quantity += add_qty
        update_inventory_file()
        print("Stock updated successfully.")
    except ValueError:
        print("Invalid quantity entered.")

def search_shoe():
    code = input("Enter shoe code to search: ").strip()
    for shoe in shoe_list:
        if shoe.code == code:
            print("Shoe found:")
            print(shoe)
            return
    print("Shoe not found.")

def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} - Value: ${value:.2f}")

def highest_qty():
    if not shoe_list:
        print("Shoe list is empty.")
        return
    highest = max(shoe_list, key=lambda x: x.get_quantity())
    print(f"{highest.product} is available for SALE! (Quantity: {highest.get_quantity()})")

def update_inventory_file():
    try:
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                file.write(line)
    except Exception as e:
        print(f"Failed to update inventory file: {e}")

#==========Main Menu=============
def main_menu():
    read_shoes_data()

    while True:
        print("\n====== SHOE INVENTORY MENU ======")
        print("1. View all shoes")
        print("2. Add new shoe")
        print("3. Restock shoe")
        print("4. Search shoe by code")
        print("5. Calculate value per item")
        print("6. Show shoe on sale (highest quantity)")
        print("7. Exit")

        # To get the user input on the main menu
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            view_all()
        elif choice == '2':
            capture_shoes()
            update_inventory_file()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main_menu()