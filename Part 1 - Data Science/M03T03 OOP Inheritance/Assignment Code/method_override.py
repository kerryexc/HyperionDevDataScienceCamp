class Adult:

    def __init__(self, name, age, eye_color, hair_color):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.hair_color = hair_color
    
    def can_drive(self):
        if age > 18:
            print("Congrats", f'{self.name}', 'you can drive legally.')

# define child class
class Child:
    def __init__(self, name, age, eye_color, hair_color):
        super().__init__()

    # override
    def can_drive(self):
        if age < 18:
            print("Unfortunately, you are too young to drive.")
        else:
            print("You can drive.")


name = input("Enter your first name")
age = int(input("Enter your age"))
eye_color = input("Enter the color of your eyes.").lower()
hair_color = input("Enter your hair color.").lower()

# you must make an object thing for the user's input
person_1 = Adult(name, age, eye_color, hair_color)
person_2 = Child(name, age, eye_color, hair_color)

person_1.can_drive()

person_2.can_drive()
