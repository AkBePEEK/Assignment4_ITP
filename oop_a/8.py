class Name(object):
    def __init__(self, firstname, lastname):
        self.fname = firstname.upper().lower().capitalize()
        self.lname = lastname.upper().lower().capitalize()
        self.fullname = self.fname + ' ' + self.lname
        self.initials = self.fname[0] + '.' + self.lname[0]


a1 = Name("john", "SMITH")
print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)