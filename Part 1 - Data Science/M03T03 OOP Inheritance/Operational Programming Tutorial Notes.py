# This is going to explain Operational Programming - Class, Inheritance

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer (Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # you do not want to copy the rest of this code; too repetitive
        # developer will handle the rest

        super().__init__(first, last, pay)
        
        # super is more manageable for multiple inheritance
        # you simply just add the new attribute to this subclass

        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        
        super().__init__(first, last, pay)
        
        if employees is None:
            # lists and dictionaries are never arguments
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):

        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):

        if emp not in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):

        for emp in self.employees:
            print('--->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# print(isinstance(mgr_1, Manager))

# Is Devloper a Subclass of Employee?
# print(issubclass(Developer, Employee))
