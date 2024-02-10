class programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        return "oof, " + str(self.salary) + ", " + str(self.work_hours)

    def compare_ps(self, programmer2):
        if self.salary > programmer2.salary or (self.salary == programmer2.salary and self.work_hours > programmer2.work_hours):
            return