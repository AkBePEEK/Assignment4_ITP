class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def people_sort(self, people_list, attribute):
        for i in range(len(people_list)):
            people_list[i].attribute


p1 = Person("Michael", "Smith", 40)
p2 = Person("Alice", "Waters", 21)
p3 = Person("Zoey", "Jones", 29)
print(people_sort([p1,p2,p3], "firstname"))