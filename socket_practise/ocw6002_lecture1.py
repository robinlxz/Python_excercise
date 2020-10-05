class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def density(self):
        return self.value / self.weight

    # def __str__(self):
    def __repr__(self):
        return f'{self.name}: <{self.value}, {self.weight}>'
        # return self.name + ': <' + str(self.value)


def buildMenu():
    wine = Food('wine', 89, 123)
    beer = Food('beer', 90, 154)
    pizza = Food('pizza', 30, 258)
    burger = Food('burger', 50, 354)
    fries = Food('fries', 90, 365)
    coke = Food('coke', 79, 150)
    apple = Food('apple', 90, 95)
    donut = Food('donut', 10, 195)
    return [wine, beer, pizza, burger, fries, coke, apple, donut]


def greedy(items, maxCost, keyFunction):
    sorted_items = sorted(items, key=keyFunction, reverse=True)
    picked_items = []
    total_cost, total_value = 0.0, 0.0
    for i in range(len(sorted_items)):
        if total_cost + sorted_items[i].getWeight() <= maxCost:
            picked_items.append(sorted_items[i])
            total_cost += sorted_items[i].getWeight()
            total_value += sorted_items[i].getValue()
    # return ([picked_items, total_value])
    return (picked_items, total_value)


menu = buildMenu()
# output = greedy(menu, 750, lambda x: x.value)
# output = greedy(menu, 750, Food.getValue)
# picked_items = output[0]
# result_value = output[1]
picked_items, result_value = greedy(menu, 750, Food.density)
# print(picked_items)
print(f' Total value: {result_value}')
for i in picked_items:
    print('  ', i)
