# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"Room | name: {self.name}, description: {self.description}, n_to: {self.n_to}, s_to: {self.s_to}, e_to: {self.e_to}, w_to: {self.w_to}"

