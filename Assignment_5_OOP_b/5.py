class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = (True if (population > 250000000 or area > 3000000) else False)

    def compare_pd(self, country):
        if self.population / self.area > country.population / country.area:
            return self.name + " has a larger population density than " + country.name
        else:
            return self.name + " has a smaller population density than " + country.name


australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)
print(australia.is_big)
print(andorra.is_big)
print(andorra.compare_pd(australia))