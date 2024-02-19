class IceCream:
    sweetness_val = {"Vanilla": 5, "Plain": 0, "ChocolateChip": 5, "Strawberry": 10, "Chocolate": 10}

    def __init__(self, flavor, num_sprinkles):
        self.flavor = flavor
        self.num_sprinkles = num_sprinkles


def sweetest_icecream(A, n=0):
    for elem in A:
        if IceCream.sweetness_val[elem.flavor] + elem.num_sprinkles > n:
            n = IceCream.sweetness_val[elem.flavor] + elem.num_sprinkles
    return n


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)
print(sweetest_icecream([ice1, ice2, ice3, ice4, ice5]))
print(sweetest_icecream([ice3, ice1]))
print(sweetest_icecream([ice3, ice5]))