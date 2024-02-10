def calculate_circumference(R):
    if 0 < R <= 10:
        return round(2 * 3.14 * R, 2)


print(calculate_circumference(10))