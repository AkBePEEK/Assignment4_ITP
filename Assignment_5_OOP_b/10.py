class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @classmethod
    def from_strings(cls, string):
        firstname, lastname, salary = string.split('-')
        return cls(firstname, lastname, salary)


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_strings("John-Smith-55000")
print(emp1.firstname)
print(emp1.salary)
print(emp2.firstname)
print(emp2.salary)