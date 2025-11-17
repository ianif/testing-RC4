from inventory import Inventory
from utils import calculate_discount, send_email  # email function doesn't exist
import json

def main():
    inv = Inventory()

    # runtime bug: wrong argument type
    inv.add_item("banana", "10")   # quantity should be int

    price = 100
    # logic bug: discount is miscalculated
    discounted = calculate_discount(price, 150)  # discount > 100, unrealistic

    print("Final price is: " + discounted)  # BUG: concatenating int to string

    # unused variable
    data = json.dumps({"a": 1})

if __name__ == "__main__":
    main()
