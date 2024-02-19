class Person(object):
    def __init__(self, name, food1, food2):
        self.name = name
        self.foodlike = food1
        self.foodhate = food2

    def taste(self, food):
        if food in self.foodlike:
            return self.name + " eats the " + food + " and loves it!"
        elif food in self.foodhate:
            return self.name + " eats the " + food + " and hates it!"
        else:
            return self.name + " eats the " + food + "!"


p1 = Person("Sam", ["ice cream"], ["carrot"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrot"))