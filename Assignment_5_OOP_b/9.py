class OnesThreesNines:
    def __init__(self, var):
        self.answer = var

    def __str__(self):
        return f"nines:{self.answer // 9}, threes:{self.answer % 9 // 3}, ones:{self.answer % 9 % 3}"


ones_threes_nines = OnesThreesNines
print(ones_threes_nines(10))
print(ones_threes_nines(15))
print(ones_threes_nines(22))