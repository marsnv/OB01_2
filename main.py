class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

магазин1 = Store("Фруктовый рынок", "Улица Яблочная, 123")
магазин2 = Store("Овощной рынок", "Проспект Морковный, 456")
магазин3 = Store("Продуктовый магазин", "Бульвар Банановый, 789")

магазин1.add_item("яблоки", 0.5)
магазин1.add_item("бананы", 0.75)
магазин2.add_item("морковь", 0.3)
магазин2.add_item("картофель", 0.4)
магазин3.add_item("молоко", 1.0)
магазин3.add_item("хлеб", 1.2)

print(магазин1.name)
магазин1.add_item("апельсины", 0.6)
print(магазин1.items)
магазин1.update_price("яблоки", 0.55)
print(магазин1.items)
магазин1.remove_item("бананы")
print(магазин1.items)
цена = магазин1.get_price("апельсины")
print(цена)
цена = магазин1.get_price("бананы")
print(цена)
