"""
The Dugout
  1. Running
  2. Baseball
  3. Basketball
  4. Exit
Select the number of a department

Attributes:
    - name
    - departments

Optional extra attributes:
    - Store hous
    - Store capacity
"""

from departments import Department
from products import Clothing, Sword

# Composition a has-a relationship (Store depends on Department, 
# Department is  instantiated inside the class)

# Aggregation: a "has-a" relationship (Department is instantiated 
# outside of the class)

# Polymorphism: works with different data structures

class Store:
    # self is the instance of the class
    # you can use **kwargs
    # __init__(self, **kwargs):
    def __init__(self, name, departments=[]):  
        self.name = name
        self.departments = departments

        # for dep in departments:
        #     department = Department(dep)
        #     self.departments.append(department)

    # for printing out
    def __str__(self):
        output = ""
        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department) + "\n"
            # or department.name

        output += str(len(self.departments) + 1) + ". Exit"
        return output

    # like string but supposed to be more specific
    # to use in debugging
    # def __repr__(self):
    #     return f"Store name is {self.name}"
        
running_products = [
        Clothing("shorts", 45, "S", "Black"),
        Clothing("sweat band", 12, "L", "Red")
        ]

fencing_products = [
        Sword("epee", 75, 10),
        Sword("Saber", 75, 4),
        ]

# Aggregation
dugout_departments = [
        Department("Running", running_products),
        Department("Baseball"),
        Department("Basketball"),
        Department("Fencing", fencing_products)
        ]

store = Store("The Dugout", dugout_departments)

print(store)

selection = 0
while selection != len(store.departments) + 1:
    selection = input( "Select the number of a department. " )

    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) +1:
            print(f"the user selected {selection}")
        elif selection == len(store.departments) + 1:
            print("Thank you for shopping with us today")
            # sys.exit()  # stops the program here
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number.")

