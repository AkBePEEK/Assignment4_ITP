class Employee(object):
    firstname = ""
    lastname = ""

    def __init__(self, name, surname):
        self.firstname = name
        self.lastname = surname
        self.email = self.firstname.lower() + "." + self.lastname.lower() + "@company.com"
        self.fullname = self.firstname + " " + self.lastname


emp1 = Employee("John", "Smith")
emp2 = Employee("Mary", "Sue")
emp3 = Employee("Antony", "Walker")
print(emp1.fullname)
print(emp2.email)
print(emp3.firstname)