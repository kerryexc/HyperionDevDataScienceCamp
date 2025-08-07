class Course:
    # Class attribute for the course name
    name = "Fundamentals of Computer Science"

    # Class attribute for the contact website
    contact_website = "www.hyperiondev.com"

    # Class attribute for office location
    office_location = "Cape Town"

    # Method to display contact details
   
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    
    # Method to display office details

    def office_details(self):
        print("The head office location is", self.office_location)


# Example usage:
# Create an instance of the Course class
course = Course()

# Call the contact_details method to display contact and office information
course.contact_details()
course.office_details()

# Create a subclass of the course class called OOPCourse

class OOPCourse(Course):
    
    description = "OOP Fundamentals"

    trainer = "Mr. Anon A. Mouse"

    id = "#12345"

    def trainer_details(self):
        print("The course if about", self.description, "taught by", self.trainer)
    
    def show_course_id(self):
        print("The course id is", self.id)

course_1 = OOPCourse()

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
