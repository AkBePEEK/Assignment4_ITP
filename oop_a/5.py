class Player(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        print(self.name, "is age", self.age)

    def get_height(self):
        print(self.name, "is height", str(self.height) + "cm")

    def get_weight(self):
        print(self.name, "is weight", str(self.weight) + "kg")


p1 = Player("David Jones", 25, 175, 75)
p1.get_age()
p1.get_height()
p1.get_weight()