class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, Adil):
        if self.age < Adil.age:
            print(Adil.name, "is older than me")
        elif self.age > Adil.age:
            print(Adil.name, "is younger than me")
        else:
            print(Adil.name, "is the same age as me")


p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2)
p2.compare_age(p1)
p1.compare_age(p3)