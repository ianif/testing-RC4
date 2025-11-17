from inventory import Inventory

def test_add_item():
    inv = Inventory()
    inv.add_item("apple", 10)
    assert inv.total_items() == 10
