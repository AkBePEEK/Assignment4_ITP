def calculate_total_gdp_fluctuation(f1, f2):
    if -100 < f1 < 100 and -100 < f2 < 100:
        return round((f2 - f1) / f1, 6)


print(calculate_total_gdp_fluctuation(10, 20))