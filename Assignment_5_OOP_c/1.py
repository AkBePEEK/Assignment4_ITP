class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


def people_sort(people_list, attribute):
    return sorted(people_list, key=lambda x: x.attribute)


p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
print(people_sort([p1,p2,p3], "firstname"))