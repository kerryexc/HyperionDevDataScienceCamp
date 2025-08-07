#Write a program that allows a user to register students for an exam venue.


#Ask user how many students are registering.
#Use input () to get user input.
student_register = int(input("How many students are registering?"))

#make an empty list for the id number
#Create a FOR LOOP that runs for that number of students

id_numbers = []
   
for i in range (0, student_register):
    id_number = (int(input("Please enter student ID numbers.")))
    id_numbers.append(id_number) 

with open('reg_form.txt', 'a') as file:
   file.write("Student ID numbers:\n")

for id_num in id_numbers:
    file.write(str(id_num) + "\n}")
    
print ("Thank you, ID numbers saved to txt file reg_form")

file.close()