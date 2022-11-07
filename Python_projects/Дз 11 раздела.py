class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


def sweetest_icecream(lst):
    flavor_values = {
        'Plain': 0,
        'Vanilla': 1,
        'ChocolateChip': 5,
        'Strawberry': 10,
        'Chocolate': 10
    }

    return max([IceCream.sprinkles + flavor_values[IceCream.flavor] for IceCream in lst])


ice1 = IceCream("Chocolate", 13)
ice2 = IceCream("Vanilla", 0)
ice3 = IceCream("Strawberry", 7)
ice4 = IceCream("Plain", 18)
ice5 = IceCream("ChocolateChip", 3)

IceCream.sweetest_icecream([ice1, ice2, ice3])
