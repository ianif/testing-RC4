import time
from inventory import Inventory

inv = Inventory()

start = time.time()
for i in range(1000):
    inv.add_item("item"+str(i), i)
end = time.time()

print("[LOG] Runtime:", end - start)
