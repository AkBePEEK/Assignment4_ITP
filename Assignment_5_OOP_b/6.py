class programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        return "oof, " + str(self.salary) + ", " + str(self.work_hours)


prog = programmer(25000, 5)
print(prog.salary)
print(prog.work_hours)
del prog
