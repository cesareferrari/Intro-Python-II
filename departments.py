class Department:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def __str__(self):
        output = ""
        output += self.name + "\n"

        for index, product in enumerate(self.products):
            output += str(index + 1) + ". " + str(product) + "\n"

        return output
