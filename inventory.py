from database import save_item

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, qty):
        self.items.append({"name": name, "qty": qty})
        save_item(name, qty)

    def total_items(self):
        total = 0
        for item in self.items:
            total = total + item["qty"]
        return total
