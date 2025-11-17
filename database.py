import sqlite3

# SECURITY BUG: hardcoded credentials
DB_PASSWORD = "123456"

def connect():
    return sqlite3.connect("inventory.db")

def save_item(name, qty):
    db = connect()
    cur = db.cursor()

    # SQL injection vulnerability
    cur.execute(f"INSERT INTO items VALUES ('{name}', {qty})")
    db.commit()
    db.close()

# unreachable code
print("Database module loaded!")
