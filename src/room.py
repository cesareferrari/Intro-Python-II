# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None

    def __str__(self):
        return f"Room - name: {self.name}, description: {self.description}, n_to: {self.n_to}"

    # def n_to(self, new_value):
    #     self.n_to = new_value
    #     return n_to




# n_to, s_to, e_to, and w_to


room1 = Room("Outside Cave Entrance", "North of you, the cave mount beckons")
room2 = Room("Foyer", "Some description")

print(room1)
print("\nroom1.n_to", room1.n_to)

room1.n_to = room2

print("\nroom1", room1)
