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

# Composition a has-a relationship
# Polymorphism: works with different data structures

class Store:
    # self is the instance of the class
    # you can use **kwargs
    # __init__(self, **kwargs):
    def __init__(self, name, departments):  
        self.name = name
        self.departments = []

        for dep in departments:
            department = Department(dep)
            self.departments.append(department)

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
        

store = Store("The Dugout", [Department("Running"), Department("Baseball"),
    Department("Basketball")])

print(store)

selection = 0
while selection != len(store.departments) + 1:
    selection = input( "Select the number of a department. " )

    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) +1:
            print(f"the user selected {selection}")
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number.")

print("Thank you for shopping")
